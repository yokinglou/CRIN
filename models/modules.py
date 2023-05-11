import torch
import torch.nn as nn
import torch.nn.functional as F

class CRF(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, xyz, normal):
        """
        Calculate CRFs of each point
        Input: 
            xyz: [B, 3, N]
            normal: [B, 3, N]
        Return:
            crf: [B, N, 3, 3]
        """
        B, C, N = xyz.shape
        device = xyz.device
        xyz = xyz.permute(0,2,1)
        normal = normal.permute(0,2,1)
        
        # PCRF 1
        z_axis = torch.Tensor([0,0,1]).to(device).view(1,1,1,3).repeat(B,N,1,1)
        w1_axis = xyz.unsqueeze(2)
        w1_axis = w1_axis / torch.clamp(w1_axis.norm(dim=-1, keepdim=True), min=1e-5)
        u1_axis = torch.cross(z_axis, w1_axis, dim=-1)
        u1_axis = u1_axis / torch.clamp(u1_axis.norm(dim=-1, keepdim=True), min=1e-5)
        v1_axis = torch.cross(w1_axis, u1_axis)
        b1 = torch.cat([u1_axis, v1_axis, w1_axis], dim=2)
        b1 = b1.transpose(2, 3)

        # PCRF 2
        w2_axis = (normal.unsqueeze(2) @ b1)
        w2_axis = w2_axis / torch.clamp(w2_axis.norm(dim=-1, keepdim=True), min=1e-5)
        u2_axis = torch.cross(z_axis, w2_axis, dim=-1)
        u2_axis = u2_axis / torch.clamp(u2_axis.norm(dim=-1, keepdim=True), min=1e-5)
        v2_axis = torch.cross(w2_axis, u2_axis)
        b2 = torch.cat([u2_axis, v2_axis, w2_axis], dim=2)
        b2 = b2.transpose(2, 3)

        crf = b1 @ b2
        return crf