这个项目是基于开源项目https://github.com/ankush-me/SynthText修改的
This project is based on the open-source project https://github.com/ankush-me/SynthText
原项目仅仅提供英文的文字的生成
It only provides the method to generate English text images in the original project
我在这里增加了中文的生成方法，添加了中文字库
I add the method to generate Chinese ones.
以及在cut.py中，会将文字裁剪出来，并且将其对应的label保存下来
cut.py can cut text out as isolate images and save their corresponding labels.
裁剪好的样例图片存放在cut-pics压缩包中
Sample cut-out images could be seen in tar "cut-pics"

-By CatWang

以下原内容



#SynthText
Code for generating synthetic text images as described in ["Synthetic Data for Text Localisation in Natural Images", Ankush Gupta, Andrea Vedaldi, Andrew Zisserman, CVPR 2016](http://www.robots.ox.ac.uk/~vgg/data/scenetext/).


**Synthetic Scene-Text Image Samples**
![Synthetic Scene-Text Samples](samples.png "Synthetic Samples")

The library is written in Python. The main dependencies are:

```
pygame, opencv (cv2), PIL (Image), numpy, matplotlib, h5py, scipy
```

###Generating samples

```
python gen.py --viz
```

This will download a data file (~56M) to the `data` directory. This data file includes:

  - **dset.h5**: This is a sample h5 file which contains a set of 5 images along with their depth and segmentation information. Note, this is just given as an example; you are encouraged to add more images (along with their depth and segmentation information) to this database for your own use.
  - **data/fonts**: three sample fonts (add more fonts to this folder and then update `fonts/fontlist.txt` with their paths).
  - **data/newsgroup**: Text-source (from the News Group dataset). This can be subsituted with any text file. Look inside `text_utils.py` to see how the text inside this file is used by the renderer.
  - **data/models/colors_new.cp**: Color-model (foreground/background text color model), learnt from the IIIT-5K word dataset. 
  - **data/models**: Other cPickle files (**char\_freq.cp**: frequency of each character in the text dataset; **font\_px2pt.cp**: conversion from pt to px for various fonts: If you add a new font, make sure that the corresponding model is present in this file, if not you can add it by adapting `invert_font_size.py`).

This script will generate random scene-text image samples and store them in an h5 file in `results/SynthText.h5`. If the `--viz` option is specified, the generated output will be visualized as the script is being run; omit the `--viz` option to turn-off the visualizations. If you want to visualize the results stored in  `results/SynthText.h5` later, run:

```
python visualize_results.py
```
### Pre-generated Dataset
A dataset with approximately 800000 synthetic scene-text images generated with this code can be found [here](http://www.robots.ox.ac.uk/~vgg/data/scenetext/).


### Further Information
Please refer to the paper for more information, or contact me (email address in the paper).
