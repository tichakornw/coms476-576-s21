## Lab 04

Note: make sure you have run `source path_to_catkin/devel/setup.bash` in all the terminals before executing the following commands.

#### Build your first robot model (URDF)

Visualize the `myfirst` model with the command

```
roslaunch urdf_demo view_urdf.launch
```

and in the other terminal, run `rviz` with the command

```
rosrun rviz rviz
```

Then follow the steps in the slides.



#### Visualize UR 10 robot model (XACRO)

Visualize the `ur 10` model

```
roslaunch ur10_description view_ur10.launch 
```

and in the other terminal, run `rviz` with the command

```
rosrun rviz rviz
```

