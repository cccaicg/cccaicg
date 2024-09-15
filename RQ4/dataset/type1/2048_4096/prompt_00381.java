/**
 * Provides a scheduler on which {@link io.reactivex.Flowable} / {@link io.reactivex.Single}
 * or {@link io.reactivex.Completable} will be subscribed.
 * <p/>
 * @see com.pushtorefresh.storio3.operations.PreparedOperation#asRxFlowable(BackpressureStrategy)
 * @see com.pushtorefresh.storio3.operations.PreparedOperation#asRxSingle()
 * @see PreparedCompletableOperation#asRxCompletable()
 *
 * @return the scheduler or {@code null} if it isn't needed to apply it.
 */
@NonNull
public CompleteBuilder defaultRxScheduler(@Nullable Scheduler defaultRxScheduler) 
{
    this.defaultRxScheduler = defaultRxScheduler;
    return this;
}   