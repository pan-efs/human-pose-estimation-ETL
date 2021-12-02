#!/usr/bin/python
import json
from dataclasses import dataclass
from typing import Dict, List
from PIL import Image

import torch
import torchvision.transforms as T
from torchvision import models


@dataclass(frozen=True)
class Joints:

    joints17 = [
        "nose",
        "left_eye",
        "right_eye",
        "left_ear",
        "right_ear",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_wrist",
        "right_wrist",
        "left_hip",
        "right_hip",
        "left_knee",
        "right_knee",
        "left_ankle",
        "right_ankle"
    ]


class DetectBodyKeypoints(Joints):

    def __init__(self):
        self.model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()
    
    
    @staticmethod
    def _normalize(img):
        t = T.Compose([T.Resize(256), 
                       T.CenterCrop(224),
                       T.ToTensor(), 
                       T.Normalize(
                            mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225])])
        
        return t(img).unsqueeze(0)

    
    def get_body_keypoints(self, 
            img_path: str, 
            threshold=0.7
        ) -> List:
        
        img = Image.open(img_path)

        with torch.no_grad():
            img_t = T.ToTensor()(img)
            img_t = img_t.unsqueeze(0)

            if next(self.model.parameters()).is_cuda:
                img_t = img_t.pin_memory().cuda(non_blocking=True)

            pred = self.model(img_t)[0]

        boxes, keypoints  = pred['boxes'], pred['keypoints'] 
        box_scores, keypoints_scores = pred['scores'], pred['keypoints_scores']

        index = [i for (i,s) in enumerate(box_scores) if s > threshold]
        result = [(boxes[i].cpu().numpy(), keypoints[i].cpu().numpy()) for i in index]

        return result
    

    def _json(self, predictions: list) -> Dict:
        joints = DetectBodyKeypoints.joints17

        det = [j for (_,j) in predictions]
        result = []

        for key in det:
           _dict = {n: k.round().astype(int).tolist() for (n,k) in zip(joints,key)}
           result.append(_dict)

        return json.dumps(result), _dict
