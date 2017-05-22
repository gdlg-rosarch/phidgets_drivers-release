Name:           ros-kinetic-phidgets-imu
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS phidgets_imu package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/phidgets_imu
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-imu-filter-madgwick
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-phidgets-api
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-phidgets-api
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf

%description
Driver for the Phidgets Spatial 3/3/3 devices

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon May 22 2017 Martin Guenther <martin.guenther@dfki.de> - 0.7.1-0
- Autogenerated by Bloom

* Fri Feb 17 2017 Martin Guenther <martin.guenther@dfki.de> - 0.7.0-0
- Autogenerated by Bloom

