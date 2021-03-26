# xWallet
Offline / online crypto wallet.


xWallet aims to create a flexible platform for storing multiple types of crypto currency on a single machine without the need of cloud based wallet systems. The wallet could be used both offline for security purposes (cold crypto storage with no network connections) but could also be used to send out transactions or receive transactions.

Please note that xWallet is a work in progress and some features may still need drastic work before they are consumer ready. If you have any suggestions for features please let me know and I'll try to add them in. 

xWallet is written completely using Python and uses DearPyGui as the main interface framework. Bitcoin Lib is also used to manage, recover and create wallets on your machine. The wallet uses a local database system inherited from Bitcoin Lib as a means of storing wallet data. 

![alt text](https://i.imgur.com/ePv1coe.png)


## Creating your first wallet


1) In the upper right corner you will see a " + " button that you can press.

![alt text](https://i.imgur.com/1pLBu9F.png)

2) You will be prompted with a menu that looks like this:

![alt text](https://i.imgur.com/NFdU9KM.png)

Choose the desired crypto currency you want to store and press "Create wallet". After the mnemonic is created make sure you also press "Copy mnemonic to clipboard" and save it somewhere where you won't lose it!

Saving your mnemonic guarantees that in a situation where you wallet is lost you can easily recover it using the "Recover wallet" tab.

Press "Back" which will bring you to the main menu and youre done!

3) Enjoy your new crypto wallet. You can now press the "Details" button for each existing wallet which will present you with some information you may want to get familiar with, its here where you can find the address of your wallet, your last transaction and the WIF key.


![alt text](https://i.imgur.com/VP2yLek.png)


## This project has been a massive learning curve and I would like to thank:

- https://github.com/hoffstadt and https://github.com/Pcothren for their amazing work on DearPyGui, repo which can be found at https://github.com/hoffstadt/DearPyGui
- https://github.com/1200wd for the work on https://github.com/1200wd/bitcoinlib which my project heavily relies on !

Support this project with some crypto !

BTC - 39MDueVQMqbs62YPrAo2WEeSi6PGAUQcNe
BCH - qq24stel6fdmql6xuxrakkma4duprw3ctue5dcsx6v
ETH - 0xdFBD2D9629701BFd7AD40C27F750d52797c680dA


