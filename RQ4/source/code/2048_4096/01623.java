//打开相机动作
@Override
    protected void onSaveInstanceState(Bundle outState){
        super.onSaveInstanceState(outState);
        outState.putParcelable("takePhotoUri", mTakePhotoUri);
        outState.putString("photoTargetFolder", mPhotoTargetFolder);
    }