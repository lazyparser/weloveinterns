

from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt


# Load a pretrained model

net = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)


# Pre-process an image


im_fname = utils.download('https://github.com/dmlc/web-data/blob/master/' +
                          'gluoncv/detection/street_small.jpg?raw=true',
                          path='street_small.jpg')
x, img = data.transforms.presets.ssd.load_test(im_fname, short=512)
print('Shape of pre-processed image:', x.shape)


# Inference and display


class_IDs, scores, bounding_boxs = net(x)

ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
                         class_IDs[0], class_names=net.classes)
plt.show()
