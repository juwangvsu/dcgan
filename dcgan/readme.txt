dcgan 5/29/24

conda activate voice
python main.py --dataset mnist --dataroot .

------------------ 7/23/24 netD.zero_grad() -----
before backward for generator, not in original
[24/25][936/938] Loss_D: 0.0003 Loss_G: 9.1786 D(x): 0.9998 D(G(z)): 0.0002 / 0.0001
[24/25][937/938] Loss_D: 0.0002 Loss_G: 9.3435 D(x): 1.0000 D(G(z)): 0.0002 / 0.0001

output:
	weights/mnist_72324/*pth
	test_images/mnist_72324/*png
------------------7/24/24 rerun original on mnist-------------------------------

output:
	e.log
	weights/mnist_72324/*pth
	test_images/mnist_72324/*png
