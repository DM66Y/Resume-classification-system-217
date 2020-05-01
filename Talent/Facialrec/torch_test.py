import os
from main_esr9 import image
from main_esr9 import video

def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        if os.path.splitext(filename)[1] == '.mp4':
            # print(filename)
            input = os.path.join(directory_name, filename)
            # print (wholepath1)
            #a = cv2.VideoCapture(wholepath1)
            #args.mode = "video"
            print("视频模式：")
            #args.input = wholepath1
            try:

                res=video(input_video_path=input, display=False, gradcam=False, output_csv_file=None, screen_size=3, device=False, frames=1,
                      branch=False, no_plot=False, face_detection=1)
                print(res)
                result = res[0]
                if result == 'Happy' or result == 'Surprise':
                    emotion = "良好的积极性和抗压能力"
                else:
                    if result == 'Fear' or result == 'Neutral':
                        emotion = "工作积极性一般"
                    else:
                        emotion = "抗压能力一般"
                print(emotion)
            except RuntimeError as e:
                print(e)


        if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.jpeg' or \
                                os.path.splitext(filename)[1] == '.png':
                # print(filename2)
                input = os.path.join(directory_name, filename)
                # print (wholepath2)
                #b = cv2.imread(wholepath2)
                #args.mode = "image"
                print("图像模式：")
                #args.input = wholepath2
                try:

                    res =image(input, display=False, gradcam=False, output_csv_file=None, screen_size=3, device=False, branch=False,
                          face_detection=1)
                    result = res[0]
                    if result == 'Happy' or result == 'Surprise':
                        emotion = "良好的积极性和抗压能力"
                    else:
                        if result == 'Fear' or result == 'Neutral':
                            emotion = "工作积极性一般"
                        else:
                            emotion = "抗压能力一般"
                    print(emotion)
                except RuntimeError as e:
                    print(e)





if __name__ == '__main__':
    read_directory(r"/home/gpz/Desktop/test/")