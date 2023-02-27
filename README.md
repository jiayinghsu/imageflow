# Parallel Processing Large Bio Image Datasets

## Distributed processing of large nD datasets across computer clusters using Daisy

Enhancing image quality is the main goal of digital image processing followed by feature extraction and categorization. Image processing has been used in fields like computer vision, medicine, meteorology, astronomy, remote sensing, and others. The primary challenge is that it takes a lot of time to complete tasks in general. Parallel computing offers an effective and practical solution to this problem. Primarily, I used Daisy to resolve this challenge at work for handling spatial transcriptomic datasets because this package is tasked with creating a scalable and quick distributed block-wise scheduler for processing very big (3D/4D bio imaging datasets ranging from TBs to PBs) datasets. We require a scheduler that is quick and scalable, but also resilient to faults and recoverable or resumeable in the event of hardware problems.

> ### Daisy chains complex pipelines of tasks

> "* Inspired by powerful workflow management frameworks like [Luigi](https://github.com/spotify/luigi) for automating long running tasks and decreasing overall processing time through task pipelining, Daisy allows user to specify dependency between tasks, allowing for task chaining and running multiple tasks in a pipeline with dynamic concurrent per-block execution."

> "* For instance, Daisy can chain a `map` task and a `reduce` task to implement a `map-reduce` task for nD datasets. Of course, any other combinations of `map` and `reduce` tasks are composable."

> "* By tracking dependencies at the `block` level, tasks can be executed concurrently to maximize pipelining parallelism."


> ### Daisy is tuned for processing datasets with real-world units

> "* Daisy has a native inferface to represent of regions in a volume in real world units, easily handling voxel sizes, with convenience functions for region manipulation (intersection, union, growing or shrinking, etc.)"

## Work in progress 
- [ ] Test different variety of images. 
- [ ] Test high level image processing algorithm.
