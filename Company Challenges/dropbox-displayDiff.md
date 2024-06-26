When a file in a user's Dropbox folder is changed, while synchronizing Dropbox tries to only upload the parts of the file that are different. The first step to accomplish this involves building a representation of the difference between the two versions of the same file.
As part of Dropbox's engineering team, you've decided to implement a function that will represent the difference between two strings in the following format:

- Two strings are merged into one.
- Text that is present in both versions is left untouched.
- Text that is present only in the old version is enclosed in parentheses ((, )).
- Text that is present only in the new version is enclosed in brackets ([, ]).
- Among all possible representations, your function returns the shortest one (brackets and parentheses do not count).
- Among representations of minimal length, your function returns the lexicographically smallest one.
- For this task, please, assume that any other character < '(' < ')' < '[' < ']'.

Now all you have to do is to implement this function.

**Example**

For:
- oldVersion = "same_prefix_1233_same_suffix"
- newVersion = "same_prefix23123_same_suffix"

The output should be: solution(oldVersion, newVersion) = "same_prefix(_1)23[12]3_same_suffix".
