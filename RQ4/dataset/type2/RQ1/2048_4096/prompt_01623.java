//打开相机动作
@Override
    protected void onSaveInstanceState(Bundle outState) 
{
    super.onSaveInstanceState(outState);
    outState.putBoolean("isSuccess", isSuccess);
    outState.putParcelable("imageUri", imageUri);
}   