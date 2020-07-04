import os
import sys

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'deepvoice3');
sys.path.append(path)

import deepvoice3
deepvoice3.synthesis(
    checkpoint_path='./tts_model.pth', 
    preset='./deepvoice3_vctk2.json', 
    dst_dir='./output/tts',
    srt_path='./subtitle.srt',
    face_path='./res.csv'
)