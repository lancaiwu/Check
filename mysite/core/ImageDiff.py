# encoding: utf-8
from PIL import Image
from PIL import ImageChops
import numpy as np
import time
from mysite.models import CheckImage, CheckImageRecord


class ImageDiff:
    # 类变量
    __xLeftOffset = 10
    __yTopOffset = 10
    __xRightOffset = 670
    __yBottomOffset = 380
    __box = (__xLeftOffset, __yTopOffset, __xRightOffset, __yBottomOffset)
    __offset = 20

    def __init__(self, imgPath, phoneNumber, uid):
        # 实例变量
        self.__time = time.time()  # 日期
        self.__img_path = None  # 原图
        self.__imgLeftIndex = None  # 原图 左起始位置
        self.__checkResultType = -1  # 结果类型
        self.__imgId = None  # 原图 数据库 id
        self.agr2 = imgPath
        self.phoneNumber = phoneNumber
        self.uid = uid

    def getEndCol(self, imagePath):
        self.__getImage1(imagePath)
        return self.__checkImage(imagePath, self.__img_path)

    def __getImageColors(self, imagePath):
        img = Image.open(imagePath)
        img = img.crop(self.__box)
        return np.array(img.convert('RGB'))

    def __getImage1(self, imgPath):
        imgRgb2 = self.__getImageColors(imgPath)
        img2LeftTop = imgRgb2[10, 10, 0]
        img2RightTop = imgRgb2[10, self.__xRightOffset - self.__xLeftOffset - 10, 0]
        img2RightBottom = imgRgb2[
            self.__yBottomOffset - self.__yTopOffset - 10, self.__xRightOffset - self.__xLeftOffset - 10, 0]
        img2LeftBottom = imgRgb2[self.__yBottomOffset - self.__yTopOffset - 10, 10, 0]
        try:
            results = CheckImage.objects.filter(img_left_top__gt=img2LeftTop - self.__offset,
                                                img_left_top__lt=img2LeftTop + self.__offset,
                                                img_right_top__gt=img2RightTop - self.__offset,
                                                img_right_top__lt=img2RightTop + self.__offset,
                                                img_right_bottom__gt=img2RightBottom - self.__offset,
                                                img_right_bottom__lt=img2RightBottom + self.__offset,
                                                img_left_bottom__gt=img2LeftBottom - self.__offset,
                                                img_left_bottom__lt=img2LeftBottom + self.__offset).first()

            if results is not None:
                self.__imgId = results.id
                self.__img_path = results.img_path
                self.__imgLeftIndex = results.left_index
            else:
                # 没有原图，将该图插入到原图数据库
                self.__insertImage('yuantu', imgPath, img2LeftTop, img2RightTop, img2RightBottom,
                                   img2LeftBottom, self.__time)
        except:
            self.__checkResultType = -1

    def __checkImage(self, imagePath, imagePath2):
        endCol = 0
        if imagePath is not None and imagePath2 is not None:
            # 原图
            img1 = Image.open(imagePath)
            img1 = img1.crop(self.__box)
            img2 = Image.open(imagePath2)
            img2 = img2.crop(self.__box)
            img3 = ImageChops.difference(img1, img2)
            img = np.array(img3.convert('RGB'))

            endCol = self.__iterColor(img, minColor=50, colsDir=-1)

            if 0 < endCol < 140:
                endCol = self.__iterColor(img, minColor=10, colsDir=-1)

            if self.__imgLeftIndex is not None:
                leftCol = self.__iterColor(img, minColor=50, colsDir=0)
                if 200 < leftCol and (self.__imgLeftIndex + 5 < leftCol or leftCol < self.__imgLeftIndex - 5):
                    # 算是原图吧，插入到数据库，替换原图
                    self.__updateImage(self.__imgId, self.agr2, leftCol, self.__time)

            # 插入记录
            self.__insertRecord(self.uid, self.phoneNumber, self.__img_path, self.agr2,
                                self.__checkResultType,
                                endCol, self.__time)
        return endCol

    def __iterColor(self, img, minColor=50, colsDir=0):
        rows, cols, colors = img.shape
        if colsDir == -1:
            colStartIndex = cols - 1
            colEndIndex = -1
            colStep = -1
        else:
            colStartIndex = 0
            colEndIndex = cols - 1
            colStep = 1
        isOk = False
        num = 0
        endCol = 0
        for j in range(colStartIndex, colEndIndex, colStep):
            if isOk and num > 90:
                self.__checkResultType = 0
                break
            for i in range(0, rows)[::-1]:
                if isOk and num > 90:
                    self.__checkResultType = 0
                    break

                # 红
                if img[i, j, 0] > minColor:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                # 绿
                if img[i, j, 1] > minColor:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                # 蓝
                if img[i, j, 2] > minColor:
                    endCol = 56 + j
                    isOk = True
                    num = num + 1
                    continue

                num = 0

            if isOk and num > 90:
                self.__checkResultType = 0
                break
        return endCol

    # 插入 记录
    def __insertRecord(self, uid, phoneNumber, imagePath1, imagePath2, checkResultType, checkResult, time):
        checkImageRecord = CheckImageRecord(phoneNumber=phoneNumber, uid=uid, imagePath1=imagePath1,
                                            imagePath2=imagePath2, checkResultType=checkResultType,
                                            checkResult=checkResult, time=time)
        checkImageRecord.save()
        return

    # 插入原图
    def __insertImage(self, img_name, agr2, img2LeftTop, img2RightTop, img2RightBottom, img2LeftBottom, time):
        checkImage = CheckImage(img_name='auto', img_path=agr2, img_left_top=img2LeftTop,
                                img_right_top=img2RightTop, img_right_bottom=img2RightBottom,
                                img_left_bottom=img2LeftBottom,
                                time=time)
        checkImage.save()
        return

    # 更新原图
    def __updateImage(self, imgId, agr2, leftIndex, time):
        try:
            checkImage = CheckImage.objects.get(id=imgId)
            checkImage.img_path = agr2
            checkImage.left_index = leftIndex
            checkImage.time = time
            checkImage.save()
        except:
            print "更新原图失败"
        return


if __name__ == '__main__':
    imgageDiff = ImageDiff('C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\screen\\mmexport1510740131806.jpeg',
                           '1571200000', '12')
    print imgageDiff.getEndCol(imgageDiff.agr2)
