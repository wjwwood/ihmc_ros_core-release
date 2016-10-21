Name:           ros-indigo-ihmc-ros-core
Version:        0.8.0
Release:        4%{?dist}
Summary:        ROS ihmc_ros_core package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://github.com/ihmcrobotics/ihmc_ros_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ros-indigo-catkin

%description
The ihmc_ros package contains several ROS packages for interacting with the IHMC
Whole Body Controller for humanoid robots.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Oct 20 2016 Doug Stephen <dstephen@ihmc.us> - 0.8.0-4
- Autogenerated by Bloom

* Thu Oct 20 2016 Doug Stephen <dstephen@ihmc.us> - 0.8.0-3
- Autogenerated by Bloom

* Thu Oct 20 2016 Doug Stephen <dstephen@ihmc.us> - 0.8.0-2
- Autogenerated by Bloom

* Thu Oct 20 2016 Doug Stephen <dstephen@ihmc.us> - 0.8.0-1
- Autogenerated by Bloom

* Wed Oct 19 2016 Doug Stephen <dstephen@ihmc.us> - 0.8.0-0
- Autogenerated by Bloom

