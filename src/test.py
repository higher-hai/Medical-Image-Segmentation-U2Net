import torch
from model import u2net_full
from torch import nn
from SEAttention import SEAttention


class my_attention(nn.Module):
    def __init__(self,):
        super(my_attention, self).__init__()
        model = u2net_full()
        netlist = list(model.children())
        self.conv0 = nn.Sequential(*model.encode_modules[:5])
        self.conv1 = model.encode_modules[5].decode_modules[0].conv
        self.se = SEAttention(channel=256, reduction=16)
        self.conv2 = model.encode_modules[5].decode_modules[0].bn
        self.conv3 = model.encode_modules[5].decode_modules[0].relu
        self.conv4 = nn.Sequential(*model.encode_modules[5].decode_modules[1:])
        self.conv5 = nn.Sequential(*model.encode_modules[6:])

    def forward(self, x):
        x = self.conv0(x)
        x = self.conv1(x)
        x = self.se(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        return x

# a = torch.randn(1, 3, 224, 224)
# my_attention = my_attention()
# out = my_attention(a)
# for i in my_attention.children():
#     print(i)
# print(out.size())
#
model = u2net_full()
netlist = list(model.children())
print(netlist[0])


# for name, module in model.named_modules():
#   if isinstance(module, nn.Conv2d):
#     print(f"Layer Name: {name}")
#     print(f"Input Channels: {module.in_channels}")
#     print(f"Output Channels: {module.out_channels}")
#     print(f"Kernel Size: {module.kernel_size}")
#     print(f"Stride: {module.stride}")
#     print(f"Padding: {module.padding}")
#     print(f"Bias: {module.bias is not None}")
#     print("-----")
