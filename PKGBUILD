# Script generated with Bloom
pkgdesc="ROS - API and ROS drivers for Phidgets devices"
url='http://ros.org/wiki/phidgets_drivers'

pkgname='ros-lunar-phidgets-drivers'
pkgver='0.7.5_1'
pkgrel=1
arch=('any')
license=('BSD, LGPL'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-libphidget21'
'ros-lunar-phidgets-api'
'ros-lunar-phidgets-high-speed-encoder'
'ros-lunar-phidgets-imu'
)

conflicts=()
replaces=()

_dir=phidgets_drivers
source=()
md5sums=()

prepare() {
    cp -R $startdir/phidgets_drivers $srcdir/phidgets_drivers
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

