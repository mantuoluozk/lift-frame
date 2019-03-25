import os
import cv2
import xml.etree.ElementTree as ET
rootpath = 'G:/VOC2012/Annotations'
zkpath = 'G:/VOC2012/JPEGImages'
outpath = 'G:/VOC2012/xml2'

for filename in os.listdir(rootpath):
#图片路径
    start,end = os.path.splitext(filename)
    imgpath = zkpath+'/'+ start +'.jpg'
#输出路径
    # outpath = outpath + '/' + start + '.png'
#xml文件路径
    xmlpath = rootpath+'/'+filename
    tree = ET.parse(xmlpath)
    root = tree.getroot()
    # print('root_tag:{}'.format(root.tag)) # .tag 节点标签名称
    # print("root_attrib:{}".format(root.attrib)) # .attrib  节点标签的属性，输出为字典
    # print("root_text:{}".format(root.text)) # .text 节点标签的内容
    # node1 = root.find("folder")  # find（）父级查找直接子级节点 ，只能获取子级的第一个 country 节点
    # print(node1.tag,node1.attrib,node1.text)
    # node2 = root.findall("object")
    # print(node2)
    # for i in node2:
    #     print("tag:{} | attrib:{} | text:{}".format(i.tag,i.attrib,i.text))

    count = 0
    for i in root:
        for j in i:
            if j.text == 'person':
                count = count + 1
                xmin = 0
                ymin = 0
                xmax = 0
                ymax = 0
                # print(j.tag,j.attrib,j.text)
                node = i.find("bndbox")
                # print(node.tag,node.attrib,node.text)
                for k in node:
                    if k.tag == "xmin":
                        # print(k.text)
                        xmin = k.text
                    elif k.tag == "ymin":
                        # print(k.text)
                        ymin = k.text
                    elif k.tag == "xmax":
                        # print(k.text)
                        xmax = k.text
                    elif k.tag == "ymax":
                        # print(k.text)
                        ymax = k.text

                img = cv2.imread(imgpath)
                cropped = img[int(ymin):int(ymax), int(xmin):int(xmax)]# 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite(outpath+ '/' + start +'_'+ str(count) +'.jpg',cropped)
    print(filename)
 
