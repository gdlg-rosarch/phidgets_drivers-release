# Script generated with Bloom
pkgdesc="ROS - Driver for the Phidgets Spatial 3/3/3 devices"
url='http://ros.org/wiki/phidgets_imu'

pkgname='ros-lunar-phidgets-imu'
pkgver='0.7.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-diagnostic-msgs'
'ros-lunar-diagnostic-updater'
'ros-lunar-nodelet'
'ros-lunar-phidgets-api'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-roslaunch'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
)

depends=('ros-lunar-diagnostic-aggregator'
'ros-lunar-diagnostic-msgs'
'ros-lunar-diagnostic-updater'
'ros-lunar-imu-filter-madgwick'
'ros-lunar-nodelet'
'ros-lunar-phidgets-api'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=phidgets_imu
source=()
md5sums=()

prepare() {
    cp -R $startdir/phidgets_imu $srcdir/phidgets_imu
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

