func hasDuplicate(nums []int) bool {
    set := map[int]struct{}{}
    for i := 0; i < len(nums); i++{
        c := nums[i]
        set[c] = struct{}{}
    }
    return len(set) != len(nums)
}
