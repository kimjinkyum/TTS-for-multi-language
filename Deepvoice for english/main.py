import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'deepvoice3');
sys.path.append(path)

import deepvoice3
from combine_generated_audio import combine

deepvoice3.synthesis(
    checkpoint_path='./source/tts/model.pth', 
    preset='./deepvoice3_vctk2.json', 
    dst_dir='./output/tts/persub',
    srt_path='./source/tts/original.txt',
    face_path='./output/detection/result.csv'
)

combine()
