import codecs
from PIL import Image
import numpy as np
import h5py
import matplotlib.pyplot as plt

from common import colorize, Color

db_fname = 'results/SynthText.h5'
db = h5py.File(db_fname, 'r')
dsets = sorted(db['data'].keys())
count = 0
print "total number of images : ", colorize(Color.RED, len(dsets), highlight=True)

with codecs.open('result.csv', 'w', encoding='utf-8') as csv:

    for k in dsets:
        m = 0
        space = 0
        space_count = 0
        rgb = db['data'][k][...]
        charBB = db['data'][k].attrs['charBB']
        wordBB = db['data'][k].attrs['wordBB']
        txt = db['data'][k].attrs['txt']

        image = Image.fromarray(rgb)


        txt_len = len(txt)

        for i in xrange(wordBB.shape[-1]):
            bb = wordBB[:, :, i]
            bb = np.c_[bb, bb[:, 0]]
            print bb[0, :]
            print bb[1, :]
            # visualize the indiv vertices:

            leftx = 1000
            lefty = 1000
            rightx = -1000
            righty = -1000

            for j in xrange(4):
                if j == 0:
                    print bb[0, j]
                    if bb[0, j] < leftx:
                        leftx = int(round(bb[0, j]))
                        # if bb[0, j] > rightx:
                        #     rightx = int(round(bb[0,j]))
                    print bb[1, j]
                    if bb[1, j] < lefty:
                        lefty = int(round(bb[1, j]))
                # if bb[1, j] > righty:
                #     righty = int(round(bb[1, j]))
                if j == 1:
                    print bb[0, j]
                    if bb[0, j] > rightx:
                        rightx = int(round(bb[0, j]))
                    print bb[1, j]
                    if bb[1, j] < lefty:
                        lefty = int(round(bb[1, j]))
                if j == 2:
                    print bb[0, j]
                    if bb[0, j] > rightx:
                        rightx = int(round(bb[0, j]))
                    print bb[1, j]
                    if bb[1, j] > righty:
                        righty = int(round(bb[1, j]))
                if j == 3:
                    print bb[0, j]
                    if bb[0, j] < leftx:
                        leftx = int(round(bb[0, j]))
                    print bb[1, j]
                    if bb[1, j] > righty:
                        righty = int(round(bb[1, j]))

            print 'result ' + str(leftx) + ', ' + str(lefty) + ', ' + str(rightx) + ', ' + str(righty)

            if leftx < 0:
                leftx = 0
            if lefty < 0:
                lefty = 0
            width, height = image.size
            if rightx > width:
                rightx = int(round(width))
            if righty > height:
                righty = int(round(height))

            print 'result11 ' + str(leftx) + ', ' + str(lefty) + ', ' + str(rightx) + ', ' + str(righty)
            print rightx
            print righty

            #
            box = (leftx, lefty, rightx, righty)
            print 'result12 ' + str(leftx) + ', ' + str(lefty) + ', ' + str(rightx) + ', ' + str(righty)
            region = image.crop(box)
            region.save('cut-pics/' + str(count) + '.jpg')
            for a in txt:
                a = a.decode('utf-8')
                print a
            list = txt[m].split('\n')
            if len(list) > 1:
                if space_count == 0:
                    space = len(list)
                if m < txt_len - 1:
                    if space_count < space:
                        csv.write('%s %s\n' % (str(count) + '.jpg', list[space_count].decode('utf-8')))
                        space_count += 1
                        count += 1
                        if space_count == space:
                            m += 1
                            space_count = 0
                else:
                    if space_count < space:
                        csv.write('%s %s\n' % (str(count) + '.jpg', list[space_count].decode('utf-8')))
                        space_count += 1
                        count += 1
                        if space_count == space:
                            m = 0
                            space_count = 0
            else:
                if m < txt_len - 1:
                    csv.write('%s %s\n' % (str(count) + '.jpg', txt[m].decode('utf-8')))
                    m += 1
                elif m == txt_len - 1:
                    csv.write('%s %s\n' % (str(count) + '.jpg', txt[m].decode('utf-8')))
                    m = 0
                count += 1


            # box = (0, 41, 150, 131)
            # region = image.crop(box)
            # region.save(str(count) + '.jpg')
            # count += 1
db.close()