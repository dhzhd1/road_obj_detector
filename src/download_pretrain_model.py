import urllib
import os

def download_pretrain_model():
    pretrain_model_path = '../pretrain_model/'
    if not os.path.exists(pretrain_model_path):
        os.mkdir(pretrain_model_path)

    model_file_name = 'resnet-101-0000.params'
    net_desc_file_name = 'resnet-101-symbol.json'
    model_url = 'http://data.dmlc.ml/mxnet/models/imagenet/resnet/101-layers/resnet-101-0000.params'
    net_desc_url = 'http://data.dmlc.ml/mxnet/models/imagenet/resnet/101-layers/resnet-101-symbol.json'
    if not os.path.isfile(os.path.join(pretrain_model_path, model_file_name)):
        data_file = urllib.URLopener()
        print("Downloading {} and saving it under {}".format(model_file_name, pretrain_model_path))
        data_file.retrieve(model_url, os.path.join(pretrain_model_path, model_file_name))
        print("Model saved under {}".format(pretrain_model_path))
    else:
        print("Pretrain model {} existed!".format(model_file_name))

    if not os.path.isfile(os.path.join(pretrain_model_path, net_desc_file_name)):
        data_file = urllib.URLopener()
        print("Downloading {} and saving it under {}".format(model_file_name, pretrain_model_path))
        data_file.retrieve(net_desc_url, os.path.join(pretrain_model_path, net_desc_file_name))
        print("Net description file saved under {}".format(pretrain_model_path))
    else:
        print("Net description file {} existed!".format(net_desc_file_name))

if __name__=='__main__':
    download_pretrain_model()