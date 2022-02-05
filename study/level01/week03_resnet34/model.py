import torch.nn as nn

def conv(in_channels, out_channels, kernel_size, stride, padding, activation=True):
    if activation:
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride, padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
    else:
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride, padding=padding),
            nn.BatchNorm2d(out_channels)
        )

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, downsample=False):
        super().__init__()

        self.channel_change = in_channels != out_channels
        self.downsample = downsample
        if downsample:
            self.layers = nn.Sequential(
                conv(in_channels, out_channels, 3, 2, 1),
                conv(out_channels, out_channels, 3, 1, 1, activation=False)
            )
            self.downsize = conv(in_channels, out_channels, 1, 2, 0, activation=False)
            self.relu = nn.ReLU(inplace=True)
        else:
            self.layers = nn.Sequential(
                conv(in_channels, out_channels, 3, 1, 1),
                conv(out_channels, out_channels, 3, 1, 1, activation=False)
            )
            self.channel = conv(in_channels, out_channels, 1, 1, 0, activation=False)
            self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        if self.downsample:
            out = self.layers(x)
            out += self.downsize(x)
            return self.relu(out)
        else:
            if self.channel_change:
                out = self.layers(x)
                out += self.channel(x)
                return self.relu(out)
            else:
                out = self.layers(x)
                out += x
                return self.relu(out)

class ResNet34(nn.Module):
    def __init__(self):
        super().__init__()

        self.unit1 = nn.Sequential(
            conv(3, 64, 7, 2, 3),
            nn.MaxPool2d(3, 2, 1)
        )
        self.unit2 = nn.Sequential(
            ResidualBlock(64, 64),
            ResidualBlock(64, 64),
            ResidualBlock(64, 64)
        )
        self.unit3 = nn.Sequential(
            ResidualBlock(64, 128, downsample=True),
            ResidualBlock(128, 128),
            ResidualBlock(128, 128),
            ResidualBlock(128, 128)
        )
        self.unit4 = nn.Sequential(
            ResidualBlock(128, 256, downsample=True),
            ResidualBlock(256, 256),
            ResidualBlock(256, 256),
            ResidualBlock(256, 256),
            ResidualBlock(256, 256),
            ResidualBlock(256, 256)
        )
        self.unit5 = nn.Sequential(
            ResidualBlock(256, 512),
            ResidualBlock(512, 512),
            ResidualBlock(512, 512)
        )
        self.avgpool = nn.AvgPool2d(2)
        self.fc = nn.Linear(512, 10)

    def forward(self, x):
        x = self.unit1(x)
        x = self.unit2(x)
        x = self.unit3(x)
        x = self.unit4(x)
        x = self.unit5(x)
        x = self.avgpool(x)
        x = x.view(x.size()[0], -1)
        x = self.fc(x)

        return x