/**
 *打开相册
 * @param requestcode  响应码
 * @param activity  上下文
 */
import android.content.Intent;
public static void toTakePicture(int requestcode, Activity activity) 
{
    Intent intent = new Intent(Intent.ACTION_PICK, null);
    intent.setDataAndType(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, "image/*");
    activity.startActivityForResult(intent, requestcode);
}   