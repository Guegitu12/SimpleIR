# -*- coding: utf-8 -*-

"""
@date: 2022/4/19 上午9:59
@file: make_query_gallery_set.py
@author: zj
@description: 创建查询集和图库
1. 针对不同的数据集格式，应该拥有不一样的划分标准。比如对于Caltech-101、oxford5k
2. 对于划分过程中的随机操作，具有可复现性
"""

import argparse

from simpleir.utils.split.build import build_splitter


def parse_args():
    parser = argparse.ArgumentParser(description="Make Query and Gallery Set")
    parser.add_argument('-d', '--dataset', metavar='DATASET', default='Caltech101', type=str, help='Dataset type')
    parser.add_argument('SRC', default='./data/caltech101/', type=str, help='Path to the src dataset')
    parser.add_argument('DST', default='./data/caltech101/', type=str, help='Path to the dst dataset')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print('args:', args)

    src_root = args.SRC
    dst_root = args.DST
    dataset_type = args.dataset

    splitter = build_splitter(dataset_type)
    splitter.run(src_root, dst_root)
