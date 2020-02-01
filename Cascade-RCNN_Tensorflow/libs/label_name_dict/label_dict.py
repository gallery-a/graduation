# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from libs.configs import cfgs

if cfgs.DATASET_NAME == 'ship':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'ship': 1
    }
elif cfgs.DATASET_NAME == 'FDDB':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'face': 1
    }
elif cfgs.DATASET_NAME == 'icdar':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'text': 1
    }
elif cfgs.DATASET_NAME.startswith('DOTA'):
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'roundabout': 1,
        'tennis-court': 2,
        'swimming-pool': 3,
        'storage-tank': 4,
        'soccer-ball-field': 5,
        'small-vehicle': 6,
        'ship': 7,
        'plane': 8,
        'large-vehicle': 9,
        'helicopter': 10,
        'harbor': 11,
        'ground-track-field': 12,
        'bridge': 13,
        'basketball-court': 14,
        'baseball-diamond': 15
    }
elif cfgs.DATASET_NAME == 'xuelang1':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'defect_1': 1
        
    }
elif cfgs.DATASET_NAME == 'xuelangplus1':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'defect_1': 1
        
    }
elif cfgs.DATASET_NAME == 'xuelang7':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'defect_1': 1,
        'defect_2': 2,
        'defect_3': 3,
        'defect_4': 4,
        'defect_5': 5,
        'defect_6': 6,
        'defect_7': 7
        
    }
elif cfgs.DATASET_NAME == 'xuelangplus7':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'defect_1': 1,
        'defect_2': 2,
        'defect_3': 3,
        'defect_4': 4,
        'defect_5': 5,
        'defect_6': 6,
        'defect_7': 7
        
    }
else:
    assert 'please set label dict!'


def get_label_name_map():
    reverse_dict = {}
    for name, label in NAME_LABEL_MAP.items():
        reverse_dict[label] = name
    return reverse_dict

LABEL_NAME_MAP = get_label_name_map()