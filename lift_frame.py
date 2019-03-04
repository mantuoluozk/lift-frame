import cv2
import os
work_dir = 'F:\\test'
dirs = os.listdir(work_dir)
for dir in dirs:
        print(dir)
        root_path = os.path.join(work_dir,dir)
        dirlist = os.listdir(root_path)
        t=0
        for n in range(0, len(dirlist)):
                path = os.path.join(root_path, dirlist[n])
                print(path)
				t=t+1
                save_path = os.makedirs(root_path + '//'+str(t).zfill(3))
                print (save_path)
                cap = cv2.VideoCapture(path)
                print (cap.isOpened())
                frame_count = 1
                success = True
                while (success):
                        success, frame = cap.read()
                        if(success):
                                params = []
                                params.append(1)
                                cv2.imwrite(root_path + '//'+str(t).zfill(3)+'//' + str(frame_count).zfill(5)+'.jpg', frame)
                                frame_count = frame_count + 1
                                print(success)
        cap.release()