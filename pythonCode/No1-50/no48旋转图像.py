#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/11 4:51 下午
# @Site    : 
# @File    : no48旋转图像.py
# @desc    : 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#            你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        右上角和左下角对折，再沿中线上下对折实现先反转270再回转180，270-180=90
        """
        len_row, len_column = len(matrix), len(matrix[0])
        if len_row == 0 or len_column == 0 or len_row != len_column:
            return
        for i in range(len_row - 1):
            for j in range(len_column - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len_row - j - 1][len_row - i - 1]
                matrix[len_row - j - 1][len_column - i - 1] = temp

        for row in range(len(matrix)):
            head, end = 0, len(matrix) - 1
            while head < end:
                for column in range(len(matrix[0])):
                    matrix[head][column], matrix[end][column] = matrix[end][column], matrix[head][column]
                head += 1
                end -= 1
        return

