## Lab 05

Note: make sure you have run `source path_to_catkin/devel/setup.bash` in all the terminals before executing the following commands.



1. In terminal 1, use `roslaunch` to start the gazebo simulator, spawn the UR 10 robot model, and load the controllers

    ```bash
    roslaunch ur10_controller gazebo_ur10.launch
    ```

2. In terminal 2, publish a one-time message to the `/elbow_joint_position_controller/command` to a single joint position controller

    ```bash
    rostopic pub /elbow_joint_positn_controller/command std_msgs/Float64 "data: -3.0" -1
    ```

    Similarly, to change the desired joint position of the `shoulder_lift_joint`, do

    ```bash
    rostopic pub /shoulder_lift_joint_position_controller/command std_msgs/Float64 "data: -0.2" -1
    ```

3. Run the simple motion planner with the command

    ```bash
    rosrun ur10_controller planner.py
    ```
    (Don't forget to mark the `planner.py` as an executable file, `chmod u+x planner.py`.)

4. To visualize all the topics and nodes, use the `rqt_graph` with the command

    ```bash
    rosrun rqt_graph rqt_graph
    ```

5. Use `rosparam` to see all the ROS parameters with

    ```bash
    rosparam list
    ```

    and you will get all the parameters

    ```
    /elbow_joint_position_controller/joint
    /elbow_joint_position_controller/pid/antiwindup
    /elbow_joint_position_controller/pid/d
    /elbow_joint_position_controller/pid/i
    /elbow_joint_position_controller/pid/i_clamp_max
    /elbow_joint_position_controller/pid/i_clamp_min
    /elbow_joint_position_controller/pid/p
    /elbow_joint_position_controller/type
    ...
    ```

6. Check the PID gains for a specific joint controller with

    ```
    rosparam get /shoulder_lift_joint_position_controller/pid
    ```

    or

    ```bash
    rosparam get /shoulder_lift_joint_position_controller/pid/p
    ```

    if you just want to see the proportional gain.

7. To change the PID gains of the controller, modify the values in the `controller/arm_controller_ur10.yaml`, and then restart the whole simulation.

8. Check the robot_description URDF model (converted from the xacro files) with the command

    ```bash
    rosparam get /robot_description
    ```

9. Check the joint angles, velocities, and torques with the command

    ```bash
    rostopic echo -n 1 /joint_state
    ```

    and the output should be something like

    ```yaml
    header: 
      seq: 128282
      stamp: 
        secs: 2566
        nsecs:  79000000
      frame_id: ''
    name: [elbow_joint, shoulder_lift_joint, shoulder_pan_joint, wrist_1_joint, wrist_2_joint,
      wrist_3_joint]
    position: [1.3506616888505105, -1.2548075128428549, 0.0010384528872879883, -1.544236818858967, -0.001346083522929753, -6.394232098797029]
    velocity: [0.17718674143857405, -0.5078291662147774, 0.05487521242823314, 2.056696997564515, 0.17388297762655924, -179.0285216068834]
    effort: [-68.48205382224303, -26.39622387730256, -1.4442390785038839, 0.7510479037128093, -2.800144745851796, -54.0]
    ```

    The `name` list actually gives the correspondence between the indices (0 - 5) and joint names. That is, `/joint_state/position[0]` is the the joint position of the `elbow_joint`.

10. You can use `rqt_gui` plot the joint angles of the robot in real time. Now suppose you have already start the `planner.py` script and the robot arm is moving repeatedly in the Gazebo simulator. Start the `rqt_gui` with

    ```bash
    rosrun rqt_gui rqt_gui
    ```

    In the menu, click `Plugins > Visualization > Plot` to open the Plot plugin.

    Next, in the `Topic` text box, enter the topic you want to plot. For example, type `/joint_states/position[0]` and click the green `+` on the right to add this topic to the plot. Thus you can see the plot of the joint angle of `elbow_joint` in real time.

    [![rqt-gui.jpg](https://i.postimg.cc/gJKTHm4B/rqt-gui.jpg)](https://postimg.cc/7Gf9xvFg)
