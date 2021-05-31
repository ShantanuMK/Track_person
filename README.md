# Track_person (Python Automation)

Want to know when a particular person is at home or not?
This simple script allows you to track that person.
If in case you want to track multiple people,
Simply create a dictionary where the key will be the IP address address of those person's device
and its value will be the person's name.
so if the detected IP address is in our dictionary, pass dict[ip_address] to say function.

Following applications can be created on basis of this script:
 
 1: ring a bell when any new device is connected to your wifi (use a set to keep a track of already connected devices ip. if new ip is not in set, ring a bell)
 
 2: having connected to some smart-lights, ac, computer, of the person's bedroom which will be automatically turn-on when that person reaches home.
 
So for example, if I came home, it will turn on my bedroom lights, my desktop, open my favorite websites, or plays my favorite playlist on Spotify (without any explicit instructions).
