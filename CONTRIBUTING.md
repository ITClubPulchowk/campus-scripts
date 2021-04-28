# Contribution Guidelines

## General

- Fork this repository to your user profile.
- Make your changes in your forked repository. Do not create a new branch.
- Open a pull request to the main repository with a meaningful message.

## Contributing scripts

- If there is not a folder of the language your script is in already (eg,
python, bash, perl, etc.), create a new directory.
- At the top of your script file include in comments - what the script does,
general usage, additional dependencies and so on. For eg, 

```bash
# this script is to manage internet connections

# dependencies it requires are nmap, NetworkManager.

# general usage of this script invovles the following commands - 
```

- Try to make sure there aren't any naming conflicts.

## Contributing Tool Guides

- Do not edit the table of contents. We'll manage that depending on the content
you have added.
- Add the related tool in the respective markdown file. If the related file 
doesn't exist yet (for eg, network-management.md as of now), create an 
appropriately named markdown file.
- Inside the markdown file, if a category for your tool doesn't exist, create
a new one.
- Any entry should contain the following parts - package required, descritpion
and usage commands/steps.

```
 ## Category name
 <one-line-description-short>

 *Package Required:* <package-and-dependencies>

 *Description:*
 <one-line-description-short>

 *Usage:*
 <usage-commands-and-optional-help-text>
```
