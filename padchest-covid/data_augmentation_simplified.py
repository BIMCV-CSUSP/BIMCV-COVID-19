# Roberto Paredes contribution @RParedesPalacios

def get_sample(self, idx):
    '''Returns the sample and the label with the id passed as a parameter'''
    # Get the row from the dataframe corresponding to the index "idx"                                                                       
    df_row = self.df.iloc[idx]
    image = Image.open(os.path.join(self.path_to_img,df_row["ImageID"]))
    da =  np.asarray(image).shape
    #image.thumbnail((self.x,self.x), Image.ANTIALIAS)                                                                                      
    image = image.resize((self.x,self.x))
    image = np.asarray(image)
    label = dict_classes[df_row["group"]]
    image_resampled = np.reshape(image,image.shape + (self.target_channels,))
    img2=np.array(image_resampled)

    img2.setflags(write=1)

    # Data aumentation **always** if True                                                                                                   
    if self.data_augmentation:
        do_rotation = True
        do_shift = True
        do_zoom = True
        do_intense= True

        theta1 = float(np.around(np.random.uniform(-10.0,10.0, size=1), 3))
        offset = list(np.random.randint(-20,20, size=2))
        zoom  = float(np.around(np.random.uniform(0.9, 1.05, size=1), 2))
        factor = float(np.around(np.random.uniform(0.8, 1.2, size=1), 2))

        if do_rotation:
            rotateit(img2, theta1)
        if do_shift:
           translateit_fast(img2, offset)


        if do_zoom:
            for channel in range(self.target_channels):
                img2[:,...,channel] = scaleit(img2[:,...,channel], zoom)
        if do_intense:
            img2[:,...,0]=intensifyit(img2[:,...,0], factor)

    #### DA ends                                                                                                                            

    img2 = self.norm(img2)
    # Return the resized image and the label                                                                                                
    return img2, label