## Simple python script to replace frontmatter properties in markdown files.

I said "be consistent in property names."

https://x.com/contentfullness/status/1757599783118877039?s=20

And I meant it.

But it turned out, I had some names in there that didn't fit the rule.

And not wanting to be a hypocrite, I made a python script that allows me to preserve my integrity.

I've tested it on a backup vault and it works just fine.

It will find and replace both words and phrases in the following way.

Publish date → publish_date
source_link → source link

It will only touch front matter properties delimited by "---"
This is to preserve the keep your notes unaltered and avoid trashing your Obsidian installation.
You can easily modify it for other purpose, just be careful.

Nevertheless, if you decide to use it, **back up your vaults** and test it on some **non-essential data** first.

Adam Ralph
17 February 2024

x.com/contentfullness

