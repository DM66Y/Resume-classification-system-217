#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO: Write docstring
"""

__author__ = "Henrique Siqueira"
__email__ = "siqueira.hc@outlook.com"
__license__ = "MIT license"
__version__ = "0.2"

# Standard Libraries
import argparse
import os
from flask import Flask,request,jsonify
import json as js
import requests
import cv2
from argparse import RawTextHelpFormatter

# Modules
from controller import cvalidation, cvision
from model.utils import uimage
from model.screen.fer_demo import FERDemo


def webcam(camera_id, display, gradcam, output_csv_file, screen_size, device, frames, branch, no_plot, face_detection):
    """
    Receives images from a camera and recognizes
    facial expressions of the closets face in a frame-based approach.

    TODO: Write docstring
    :param no_plot:
    :param camera_id:
    :param display:
    :param gradcam:
    :param output_csv_file:
    :param screen_size:
    :param device:
    :param frames:
    :param branch:
    :return:
    """
    fer_demo = None

    if not uimage.initialize_video_capture(camera_id):
        raise RuntimeError("Error on initializing video capture." +
                           "\nCheck whether a webcam is working or not." +
                           "In linux, you can use Cheese for testing.")

    uimage.set_fps(frames)

    # Initialize screen
    if display:
        fer_demo = FERDemo(screen_size=screen_size, display_individual_classification=branch, display_graph_ensemble=(not no_plot))

    try:
        # Loop to process each frame from a VideoCapture object.
        while uimage.is_video_capture_open() and ((not display) or (display and fer_demo.is_running())):
            # Get a frame
            image = uimage.get_frame()

            fer = None if (image is None) else cvision.recognize_facial_expression(image, device, face_detection, gradcam)

            # Display blank screen if no face is detected, otherwise,
            # display detected faces and perceived facial expression labels
            if display:
                fer_demo.update(fer)
                fer_demo.show()

            # TODO: Implement
            if output_csv_file:
                pass

    except Exception as e:
        print("Error raised during video mode.")
        raise e
    finally:
        uimage.release_video_capture()
        fer_demo.quit()


def image(input_image_path, display, gradcam, output_csv_file, screen_size, device, branch, face_detection):
    """
    Receives the full path to a image file and recognizes
    facial expressions of the closets face in a frame-based approach.

    TODO: Write docstring

    :param input_image_path:
    :param display:
    :param gradcam:
    :param output_csv_file:
    :param screen_size:
    :param device:
    :param branch:
    :return:
    """

    image = uimage.read(input_image_path)

    # Call FER method
    fer = cvision.recognize_facial_expression(image, device, face_detection, gradcam)

    # TODO: Implement
    if output_csv_file:
        pass

    if display:
        fer_demo = FERDemo(screen_size=screen_size, display_individual_classification=branch, display_graph_ensemble=False)
        fer_demo.update(fer)
        while fer_demo.is_running():
            fer_demo.show()
        fer_demo.quit()
    return fer

def video(input_video_path, display, gradcam, output_csv_file, screen_size, device, frames, branch, no_plot, face_detection):
    """
    Receives the full path to a video file and recognizes
    facial expressions of the closets face in a frame-based approach.

    TODO: Write docstring

    :param input_video_path:
    :param display:
    :param gradcam:
    :param output_csv_file:
    :param screen_size:
    :param device:
    :param frames:
    :param branch:
    :return:
    """
    fer_demo = None
    candidate=[]
    if not uimage.initialize_video_capture(input_video_path):
        raise RuntimeError("Error on initializing video capture." +
                           "\nCheck whether working versions of ffmpeg or gstreamer is installed." +
                           "\nSupported file format: MPEG-4 (*.mp4).")

    uimage.set_fps(frames)

    # Initialize screen
    if display:
        fer_demo = FERDemo(screen_size=screen_size, display_individual_classification=branch, display_graph_ensemble=(not no_plot))

    try:
        # Loop to process each frame from a VideoCapture object.
        while uimage.is_video_capture_open() and ((not display) or (display and fer_demo.is_running())):
            # Get a frame
            image = uimage.get_frame()

            fer = None if (image is None) else cvision.recognize_facial_expression(image, device, face_detection, gradcam)
            candidate.append(fer)
            #print(candidate)
            # Display blank screen if no face is detected, otherwise,
            # display detected faces and perceived facial expression labels
            if display:
                fer_demo.update(fer)
                fer_demo.show()

            # TODO: Implement
            if output_csv_file:
                pass
        return candidate
    except Exception as e:
        #print("Error raised during video mode.")
        return  candidate
    # finally:
    #     uimage.release_video_capture()
    #     #fer_demo.quit()


application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH']=16*1024*1024

@application.route('/api/facialrec',methods=['GET','POST'])
def facialrec():
    if request.method == "POST":
        user_id = js.loads(request.data)["user_id"]
        file_num = js.loads(request.data)["file_num"]
        file = js.loads(request.data)["file_info"]
        file_type=js.loads(request.data)["file_type"]
        if file_type== "video":
            print("视频模式：")
            try:
                res=video(input_video_path=file, display=False, gradcam=False, output_csv_file=None, screen_size=3, device=False, frames=1,
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
            json={
                "user_id":user_id,
                "result":emotion
            }
            return jsonify(json)
        if file_type == "image":

                try:

                    res =image(file, display=False, gradcam=False, output_csv_file=None, screen_size=3, device=False, branch=False,
                          face_detection=1)
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
                    json = {
                        "user_id": user_id,
                        "result": emotion
                    }
                    return jsonify(json)
                except RuntimeError as e:
                    print(e)






if __name__ == "__main__":
    application.run(host="127.0.0.1",port=4014,debug=True)

