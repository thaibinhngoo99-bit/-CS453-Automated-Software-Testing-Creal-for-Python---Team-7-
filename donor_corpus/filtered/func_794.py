def get_dataloader_single_folder(data_dir, imageFolder='Images', maskFolder='Masks', fraction=0.2, batch_size=4):
    """
        Create training and testing dataloaders from a single folder.
    """
    data_transforms = {'Train': transforms.Compose([Resize((256, 256), (256, 256)), ToTensor(), Normalize()]), 'Test': transforms.Compose([Resize((256, 256), (256, 256)), ToTensor(), Normalize()])}
    image_datasets = {x: SegDataset(data_dir, imageFolder=imageFolder, maskFolder=maskFolder, seed=100, fraction=fraction, subset=x, transform=data_transforms[x]) for x in ['Train', 'Test']}
    dataloaders = {x: DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True, num_workers=8) for x in ['Train', 'Test']}
    return dataloaders