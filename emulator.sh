#~/1_android/SDK/emulator/qemu/linux-x86_64/qemu-system-x86_64 -netdelay none -netspeed full -avd Nexus_5X_API_28_ttest
#emulator -avd Nexus_5X_API_28_ttest
#(emulator -avd Nexus_5X_API_28_ttest &)
#emulator -avd Nexus_5X_API_28_ttest & disown $!

#emulator -avd Nexus_5X_API_28_ttest &!

#nohup emulator -avd Nexus_5X_API_28_ttest

#screen
#emulator -avd Nexus_5X_API_28_ttest

#nohup emulator -avd Nexus_5X_API_28_ttest & exit

#(bash emulator -avd Nexus_5X_API_28_ttest &) &>/dev/null

bash -i >/dev/null 2>&1 <<<'nohup emulator -avd Nexus_5X_API_28_ttest &'
