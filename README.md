# Parallel Processing Large Bio Image Datasets

## Distributed processing of large nD datasets across computer clusters using Daisy

Enhancing image quality is the main goal of digital image processing, which is followed by feature extraction and categorization. It is used in fields like computer vision, imaging in medicine, meteorology, astronomy, remote sensing, and others. The primary difficulty is that it takes a lot of time to complete tasks in general; parallel computing offers an effective and practical solution to this problem.

> ### Daisy chains complex pipelines of tasks

> "* Inspired by powerful workflow management frameworks like [Luigi](https://github.com/spotify/luigi) for automating long running tasks and decreasing overall processing time through task pipelining, Daisy allows user to specify dependency between tasks, allowing for task chaining and running multiple tasks in a pipeline with dynamic concurrent per-block execution."

> "* For instance, Daisy can chain a `map` task and a `reduce` task to implement a `map-reduce` task for nD datasets. Of course, any other combinations of `map` and `reduce` tasks are composable."

> "* By tracking dependencies at the `block` level, tasks can be executed concurrently to maximize pipelining parallelism."


> ### Daisy is tuned for processing datasets with real-world units

> "* Daisy has a native inferface to represent of regions in a volume in real world units, easily handling voxel sizes, with convenience functions for region manipulation (intersection, union, growing or shrinking, etc.)"

## Work in progress 
- [ ] Test different variety of images. 
- [ ] Test high level image processing algorithm.
