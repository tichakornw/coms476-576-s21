## Lab 02 

### Install catkin_tools

Follow the instructions here:

[Installing catkin_tools — catkin_tools 0.0.0 documentation (catkin-tools.readthedocs.io)](https://catkin-tools.readthedocs.io/en/latest/installing.html)

Typically, if you are using Ubuntu 18.04, you can install `catkin_tools` via `apt-get`:

1. First you must have the ROS repositories which contain the `.deb` for `catkin_tools`:
    ```
    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
    $ wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
    ```
    
1. Once you have added that repository, run these commands to install `catkin_tools`:

	```
   $ sudo apt-get update
   $ sudo apt-get install python-catkin-tools
   ```

### catkin_make vs catkin_tools

`catkin_make` and `catkin_tools` are two build tools for ROS packages and have almost the same features. We prefer `catkin_tools` for multiple reasons:

- Good management of the ROS configuration including explicit workspace chaining instead of implicit.
- Ability to build the workspace from wherever in the directory (so you can build even if you are not in the root of the workspace).
- Easy to build single packages and blacklist others
- Easy to store `cmake` arguments so that you don't have to repeat them every time

### ROS std_msgs Types

Standard ROS Messages including common message types representing primitive data types and other basic message constructs, such as `multiarrays`. 

[std_msgs - ROS Wiki](http://wiki.ros.org/std_msgs)

For example, a `String` message is defined as

```
string data
```

### Writing Publisher and Subscriber

The code I demonstrated in the Lab 2 can be found under the `catkin_ws/src` folder. In case you have any other questions, you can email me or check the tutorial below

[ROS/Tutorials/WritingPublisherSubscriber(python) - ROS Wiki](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(python))

If you prefer to use C++, here's also a tutorial on that with full explanation:

[ROS/Tutorials/WritingPublisherSubscriber(c++) - ROS Wiki](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(c%2B%2B))

In these two tutorials, the author use the `catkin_make` command to build the packages. So if you choose to use `catkin_tools`, you need to replace it with `catkin build` as I did in the lab.