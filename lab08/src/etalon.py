import torch, lab07_lib as L
Xtr, Xte, Ftr, Fte = L.dataset(L.KINDS[1])
print("эталон, PSNR на тесте:", round(L.psnr_images(Xtr.mean(0, keepdim=True).expand_as(Xte), Xte), 3))