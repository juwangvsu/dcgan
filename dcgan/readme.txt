dcgan 5/29/24

conda activate voice
nohup python3 main.py --dataset mnist --dataroot . > e.csv 2>&1 < /dev/null &
tail -f e.csv

-------07/28/24 exp note -----------------------
i9ub22:
	mnist, epoch 19,20 generator collaps, recover at 23
alien1:
	lsun, 28+ hours
--------------------about network arch ------------------
GAN goodfellow:
	3 layers mlp with rectified linear, sigmoid for mnist
	more conv + fully connected layer, deeper, cifar
	network config using pylearn, yaml files 
	https://github.com/goodfeli/adversarial
dcgan:
	architecture see dcgan paper, conv layers, batch normal, no fc, sigmoid
	discriminator last layer conv2d() inpch(1024)x4x4, output i channel

------------------ 7/23, 25/24 netD.zero_grad() -----
before backward for generator, not in original
[24/25][936/938] Loss_D: 0.0003 Loss_G: 9.1786 D(x): 0.9998 D(G(z)): 0.0002 / 0.0001
[24/25][937/938] Loss_D: 0.0002 Loss_G: 9.3435 D(x): 1.0000 D(G(z)): 0.0002 / 0.0001

output:
	weights/mnist_zero_72324/*pth
	test_images/mnist_zero_72324/e.csv
	test_images/mnist_zero_72524/e.csv  i9ub22
------------------7/24/24 rerun original on mnist-------------------------------

output:
	e.log
	weights/mnist_72424/*pth
	test_images/mnist_72424/e.csv
[15/25][860/938] Loss_D: 0.0297 Loss_G: 5.4952 D(x): 0.9842 D(G(z)): 0.0129 / 0.0075
[15/25][863/938] Loss_D: 0.0214 Loss_G: 4.8939 D(x): 0.9928 D(G(z)): 0.0136 / 0.0124

[24/25][936/938] Loss_D: 0.0012 Loss_G: 8.0673 D(x): 0.9995 D(G(z)): 0.0007 / 0.0003
[24/25][937/938] Loss_D: 0.0031 Loss_G: 7.9569 D(x): 0.9974 D(G(z)): 0.0004 / 0.0004
