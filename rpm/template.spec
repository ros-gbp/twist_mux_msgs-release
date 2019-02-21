Name:           ros-melodic-twist-mux-msgs
Version:        2.1.0
Release:        5%{?dist}
Summary:        ROS twist_mux_msgs package

Group:          Development/Libraries
License:        CC BY-NC-SA 4.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-message-runtime
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation

%description
The twist_mux msgs and actions package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Feb 21 2019 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-5
- Autogenerated by Bloom

* Thu Feb 21 2019 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-4
- Autogenerated by Bloom

* Mon Jun 25 2018 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-3
- Autogenerated by Bloom

* Mon Jun 25 2018 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-2
- Autogenerated by Bloom

* Mon Jun 25 2018 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-1
- Autogenerated by Bloom

* Mon Jun 25 2018 Enrique Fernandez <efernandez@clearpathrobotics.com> - 2.1.0-0
- Autogenerated by Bloom

