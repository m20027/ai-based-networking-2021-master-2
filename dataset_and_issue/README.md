## ITU AI/ML in 5G Challenge Global Round in Japan (Theme 2 from NEC)
This is the dataset and issue of theme 2: Network State Estimation by Analyzing Raw Video Data.

## Problem

The goal of this challenge is to estimate network state, i.e., throughput and loss ratio, from given raw video data sets. 

The participants are expected to train and test an AI model using the video data with labels of network state in "dataset" directory and estimate network state for videos in "issue" directory.

## Files

This tarball contains following dataset and issue.

- dataset
  - original: Original files named \<video id\>.mp4
  - received: Received files named \<video id\>\_\<bitrate\>\_\<loss ratio\>.mp4

- issue
  - original: Original files named \<from problem id\>-\<to problem id\>.mp4
  - received: Received files named \<problem id\>.mp4

Note that loss ratio are expressed as follows.
  - 0001: 0.001%
  - 001 : 0.01%
  - 0025: 0.025%
  - 005 : 0.05%
  - 01  : 0.1%
  - 025 : 0.25%


