## List of known issues, todo's, questions and suggestions

### 2023-09-10 (issue)
Some screenshots contain text fields that are not aligned (see figure below). These misalignments can occur in title boxes, buttons, labels (Windows 11).

![](images/account-dividend-booking.png)

This issue seems to be related with the changing of the default font (`Help > Settings > Presentation > Formatting > Font size`). Setting it to 9px (Default) removes the issue.

### 2023-09-10 (question)
Images are stored in a subdirectory of the one where the md file resides.
``` 
concepts
   account.md
   images
      pic1.png
```
What is the correct way to reference this image?

```
1.![](images/pic1.png)
2.![](../images/pic1.png)
```

(1) seems to work, both in the texteditor (VSCode) and the website. However, the path at the website is `<img src="../images/pic1.png">` (1) is used at this moment.

(2) does not show the image in the texteditor preview but appears normally on the website. (2) is also needed is referencing the img in HTML.

### 2023-09-13 (suggestion implemented)

The mkdocs material frontmatter can contain several key-value pairs. It seems that only the title is taken into account for the material theme.

The frontmatter could contain other valuable info (already implemented)

- lastUpdate: YYYY-MM-DD
- todo: info about things todo on this page.

### 2023-09-16 (question)
Upon creating a security, you can specify a Calendar in the Security Master Data.

(1) What is this calendar used for?. According to the tooltip: These dates will affect some calculations, the display of price gaps and the execution of saving plans.  Which calculations? Does it matter for performance calculations?

(2) The content of these calendars is visible in `Help > Preferences > Calendar`. Can this be changed? Custom calendar?

(3) What's the difference between the `Apply` and `Apply and close` in the panel `Help > Preferences > Calendar`. Necessary?

### 2023-09-16 (question)
At the moment there is a top-level menu item called "Tips & tricks". Isn't this too informal? Replacing with "Advanced topics"?

Also the top-level item "Common procedures" may seem to generic. Other suggestions?

