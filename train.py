import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from model import AnimalHumanClassifier
from dataset import AnimalDataset
from config import Config
