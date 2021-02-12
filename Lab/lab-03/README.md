## Lab 03

### ROS tf2 Wiki

[tf2 - ROS Wiki](http://wiki.ros.org/tf2)

`tf2` is the second generation of the transform library, which lets the user keep track of multiple coordinate frames over time. `tf2` maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user transform points, vectors, etc between any two coordinate frames at any desired point in time.



### Related tools

* Print information about the current transform tree

  `rosrun tf tf_monitor`

* Print information about the transform between two frames

  `rosrun tf tf_echo src_frame tar_frame`

* View frames in a pdf file

  `rosrun tf view_frames`

* Visualize frames in RViz

  1. `rosrun rviz rviz`
  2. Select `world` as the fixed frame
  3. Add `tf` to visualizer

* Check `/tf` and `/tf_static` topic

  `rostopic info /tf`

  `rostopic info /tf_static`

* Visualize ROS node graph (You can check the subscriber and publisher of `/tf` and `/tf_staic` here)

  `rosrun rqt_graph rqt_graph`

### Homework

This tutorial teaches you how to broadcast coordinate frames of a robot to tf2.

* C++ 

  [tf2/Tutorials/Writing a tf2 broadcaster (C++) - ROS Wiki](http://wiki.ros.org/tf2/Tutorials/Writing a tf2 broadcaster (C%2B%2B))

* Python

  [tf2/Tutorials/Writing a tf2 broadcaster (Python) - ROS Wiki](http://wiki.ros.org/tf2/Tutorials/Writing a tf2 broadcaster (Python))



### Reference

* [Euler gimbal lock explaine - YouTube](https://www.youtube.com/watch?v=zc8b2Jo7mno)
* [Quaternions and 3d rotation, explained interactively - YouTube](https://www.youtube.com/watch?v=zjMuIxRvygQ)

