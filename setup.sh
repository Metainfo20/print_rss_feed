#!/bin/bash

f_printer_setup(){
    echo "Add current user $USER to group 'lp' for enable direct print."
    read -p "Do you wish to continue?(y/n):" yn
    case $yn in
        [Yy]* ) echo "sudo usermod -a -G lp $USER"; sudo usermod -a -G lp $USER; echo "Done. Logout required";;
        * ) echo "Exit";;
    esac
}

f_printer_test(){
    echo "Direct print test. Test symbols will be print immediately."
    read -p "Input printer location (default is /dev/usb/lp0):" location
    case $location in
        * ) echo "test_direct_print > $location"; echo "test_direct_print" > $location;;
        "") echo "Cannot be empty, aborted";;
    esac
}

f_sep(){
    echo "---------------------------"
}

while true; do
    f_sep; echo "print_rss_feed setup"; f_sep
    echo "1 - Setup new direct print access"
    echo "2 - Direct print test"; f_sep
    echo "Enter your choice:"; read choice; f_sep
    case $choice in
        "1") f_printer_setup;;
        "2")f_printer_test;;
        "exit") echo "Bye!"; exit;;
         * ) echo "Please enter valid number or input 'exit' for exit."; sleep 1s; f_sep;;
    esac
done

