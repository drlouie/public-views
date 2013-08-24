// AS1 Selection Gallery
/**
 * Gallery consisting of a set of images that can be selected with
 * mouse gestures into groups capable of being cycled or viewed individually.
 * @param target The movie clip in which to create the gallery
 * @param depth The depth in the target to create the main gallery movie clip
 * @param sourceUrl The URL of the XML containing the image information for the gallery
 * @param width The width to draw the gallery
 * @param height The height to draw the gallery
 */
function SelectionGallery(target, depth, sourceUrl, width, height){
	this.groups = [];				// array to contain all the groups currently selected
	this._listeners = [];			// listeners for event broadcasting
	this.loader = new SGSourceLoader(this);	// loader for loading XML
	this.gallery = this;			// gallery reference
	this.target = target;			// reference to target
	if (width) this.width = width;		// width of the gallery interface
	if (height) this.height = height;	// height of the gallery interface
	SGTweener.broadcaster = this;		// assign this as the broadcaster signalling SGTweener events
	
	// create movie clip containers
	this.galleryContainer = target.createEmptyMovieClip("SelectionGallery", depth);
	this.slideContainer = this.galleryContainer.createEmptyMovieClip("slideContainer", 0);
	this.selectionContainer = this.galleryContainer.createEmptyMovieClip("selectionContainer", 1);
	this.controlsContainer = this.galleryContainer.createEmptyMovieClip("controlsContainer", 2);
	this.toolTipContainer = this.galleryContainer.createEmptyMovieClip("toolTipContainer", 1000);
	
	// create instance for managing user selections
	this.userSelection = new SGUserSelection(this, this.selectionContainer);
	
	// create instance for managing tooltips
	this.toolTip = new SGToolTip(this, this.toolTipContainer);
	
	// initiate UI
	this.updateUIDimensions();
	this.initControls();
	this.drawUI();
	
	// event handlers
	this.onContent = this.contentLoaded;
	this.onSlideLoaded = this.slideLoaded;
	this.onSelection = this.slidesSelected;
	this.galleryContainer.onEnterFrame = SGEventHandler.scope(this.broadcastEnterFrame, this);
	
	// load XML if provided
	if (sourceUrl != null) this.load(sourceUrl);
}
SelectionGallery.prototype.width = 500;
SelectionGallery.prototype.height = 400;
SelectionGallery.prototype.padding = 10;
SelectionGallery.prototype.faceBorder = 10;
SelectionGallery.prototype.hudHeight = 30;
SelectionGallery.prototype.slideMargin = 10;
SelectionGallery.prototype.slidePadding = 20;
SelectionGallery.prototype.selectionColor = 0xFF9700;
SelectionGallery.prototype.faceColor = 0x000000;
SelectionGallery.prototype.itemBackgroundColor = 0xB4AF91;
SelectionGallery.prototype.backgroundColor = 0x263D48;
SelectionGallery.prototype.textColor = 0xFFFFFF;
SelectionGallery.prototype.openImages = true;
SelectionGallery.prototype.currGroup = null;
SelectionGallery.prototype.multiSelection = false;
SelectionGallery.prototype.loadCount = 0;
SelectionGallery.prototype.toString = function(){
	return "[object SelectionGallery]";
}
/**
 * Broadcasts the onEnterFrame event every frame, primarily for tweener
 */
SelectionGallery.prototype.broadcastEnterFrame = function(){
	this.broadcastMessage("onEnterFrame");
}
/**
 * Adds a listener to the selection gallery
 */
SelectionGallery.prototype.addListener = function(obj){
	this._listeners.push(obj);
}
/**
 * Removes a listener to the selection gallery
 */
SelectionGallery.prototype.removeListener = function(obj){
	var i = this._listeners.length;
	while (i--){
		if (this._listeners[i] == obj){
			this._listeners.splice(i, 1);
			break;
		}
	}
}
/**
 * Broadcasts an event to all listeners of the selection gallery
 */
SelectionGallery.prototype.broadcastMessage = function(msg){
	var lists = this._listeners.slice();
	var n = lists.length;
	var i;
	for (i=0; i<n; i++){
		lists[i][msg]();
	}
}
/**
 * Creates and adds buttons and status message text field
 */
SelectionGallery.prototype.initControls = function(){
	this.controlsContainer.createTextField("infoText", 0, 0, 0, 1, 1);
	this.infoText = this.controlsContainer.infoText;
	this.infoText.autoSize = "center";
	this.infoText.selectable = false;
	var tf = this.infoText.getTextFormat();
	tf.font = "_sans";
	this.infoText.setNewTextFormat(tf);
	var target;
	target = this.controlsContainer.createEmptyMovieClip("prevset", 1);
	this.prevButton = new SGPrevButton(this, target);
	target = this.controlsContainer.createEmptyMovieClip("closeselection", 2);
	this.closeButton = new SGCloseButton(this, target);
	target = this.controlsContainer.createEmptyMovieClip("openselection", 3);
	this.openButton = new SGOpenButton(this, target);
	target = this.controlsContainer.createEmptyMovieClip("nextset", 4);
	this.nextButton = new SGNextButton(this, target);
	this.drawControls();
}
/**
 * Draws the graphics for the controls
 */
SelectionGallery.prototype.drawControls = function(){
	var halfHud = this.hudHeight/2;
	var doubleHud = 2*this.hudHeight;
	var controlHeight = this.height - this.faceBorder - halfHud;
	this.prevButton.draw();
	this.prevButton.target._x = this.hudHeight + this.faceBorder;
	this.prevButton.target._y = controlHeight;
	this.nextButton.draw();
	this.nextButton.target._x = this.width - this.hudHeight - this.faceBorder;
	this.nextButton.target._y = controlHeight;
	this.closeButton.draw();
	this.closeButton.target._x = this.prevButton.target._x + doubleHud;
	this.closeButton.target._y = controlHeight;
	this.openButton.draw();
	this.openButton.target._x = this.nextButton.target._x - doubleHud;
	this.openButton.target._y = controlHeight;
	this.drawInfoText();
}
/**
 * Sets style and positions the info text field
 */
SelectionGallery.prototype.drawInfoText = function(){
	this.infoText.textColor = this.textColor;
	var controlHeight = this.height - this.faceBorder - this.hudHeight/2;
	this.infoText._x = this.width/2 - this.infoText._width/2;
	this.infoText._y = controlHeight - this.infoText._height/2;
}
/**
 * Sets the contents of the info text field
 */
SelectionGallery.prototype.setInfo = function(text){
	this.infoText.text = text;
	this.drawInfoText();
}
/**
 * Updates the info text field with the most up-to-date gallery state
 */
SelectionGallery.prototype.updateInfo = function(){
	if (this.currGroup.slides.length == 1){
		this.setInfo("Image: "+this.currGroup.slides[0].image.title);
	}else if (this.groups.length == 1){
		this.setInfo("Gallery: "+this.currGroup.slides.length+" images");
	}else{
		this.setInfo("Set: "+this.currGroup.slides.length+" images");
	}
}
/**
 * Defines properties used internally by the gallery based on the
 * most recent definitions set for public properties relating to the UI
 */
SelectionGallery.prototype.updateUIDimensions = function(){
	var sizeOffset = 2*(this.padding + this.faceBorder);
	this.availWidth = this.width - sizeOffset;
	this.availHeight = this.height - sizeOffset - this.hudHeight;
	this.centerX = this.width/2;
	this.centerY = (this.height - this.hudHeight)/2;
}
/**
 * Renders the current state of the gallery updating it with any new
 * definitions assigned to it relating to UI or its style
 */
SelectionGallery.prototype.draw = function(minor){
	this.updateUIDimensions();
	var n = this.groups.length;
	var i;
	for(i=0; i<n; i++){
		this.groups[i].draw(minor);
	}
	if (!minor){
		this.drawUI();
		this.drawControls();
	}
}
/**
 * Draws the interface of the gallery
 */
SelectionGallery.prototype.drawUI = function(){
	var left;
	var top;
	var right;
	var bottom;
	this.galleryContainer.clear();
	this.galleryContainer.beginFill(this.backgroundColor, 100);
	this.galleryContainer.lineTo(this.width, 0);
	this.galleryContainer.lineTo(this.width, this.height);
	this.galleryContainer.lineTo(0, this.height);
	this.galleryContainer.lineTo(0, 0);
	this.galleryContainer.endFill();
	this.galleryContainer.beginFill(this.faceColor, 100);
	this.galleryContainer.moveTo(this.width, 0);
	this.galleryContainer.lineTo(this.width, 0);
	this.galleryContainer.lineTo(this.width, this.height);
	this.galleryContainer.lineTo(0, this.height);
	this.galleryContainer.lineTo(0, 0);
	right = this.width - this.faceBorder;
	bottom = this.height - this.faceBorder;
	this.galleryContainer.moveTo(this.faceBorder, this.faceBorder);
	this.galleryContainer.lineTo(right, this.faceBorder);
	this.galleryContainer.lineTo(right, bottom);
	this.galleryContainer.lineTo(this.faceBorder, bottom);
	this.galleryContainer.lineTo(this.faceBorder, this.faceBorder);
	this.galleryContainer.endFill();
	top = this.height - this.faceBorder - this.hudHeight;
	bottom = this.height - this.faceBorder;
	right = this.width - this.faceBorder;
	SGGraphics.simpleLinearGradient(this.galleryContainer, top, this.hudHeight, this.faceColor, this.backgroundColor);
	this.galleryContainer.moveTo(this.faceBorder, top);
	this.galleryContainer.lineTo(right, top);
	this.galleryContainer.lineTo(right, bottom);
	this.galleryContainer.lineTo(this.faceBorder, bottom);
	this.galleryContainer.lineTo(this.faceBorder, this.faceBorder);
	this.galleryContainer.endFill();
}
/**
 * Prevents user selection controls from activating a selection when the mouse is released
 */
SelectionGallery.prototype.beginMultiSelection = function(){
	if (this.multiSelection) return;
	this.multiSelection = true;
	this.userSelection.selectInit();
}
/**
 * Ends a multiple selection activating all gestures made since beginMultiSelection was called
 */
SelectionGallery.prototype.endMultiSelection = function(){
	if (!this.multiSelection) return;
	this.multiSelection = false;
	this.userSelection.setSelection();
}
/**
 * Adds a new group to the gallery with the slides passed
 */
SelectionGallery.prototype.addNewGroup = function(slides){
	this.underGroup = (this.currGroup) ? this.currGroup : null;
	this.currGroup = new SGImageGroup(this, this.groups.length, slides);
	this.groups.push(this.currGroup);
	if (slides.length == 1){
		slides[0].loadFullImage();
	}
	this.updateInfo();
}
/**
 * Drops the current gallery group resorting to the group below the one being dropped
 * The slides in the group being dropped are returned to the group below
 */
SelectionGallery.prototype.dropGroup = function(){
	if (this.groups.length <= 1) return;
	if (this.currGroup.slides.length == 1){
		this.currGroup.slides[0].clearFullImage();
	}
	this.currGroup.dropSlides(null, this.underGroup);
	this.currGroup = this.underGroup;
	this.groups.pop();
	var underIndex = this.groups.length - 2;
	this.underGroup = (underIndex >= 0) ? this.groups[underIndex] : null;
	this.updateInfo();
}
/**
 * Opens the next active selection for the gallery.  This can be either a single slide
 * or a group if a group has recently been dropped 
 */
SelectionGallery.prototype.openSelection = function(){
	if (this.currGroup.slides.length == 1){
		if (this.openImages){
			getURL(this.currGroup.slides[0].image.url, "_blank");
		}
		return;
	}
	var slides = (this.currGroup.sets.length) 
		? this.currGroup.sets[0]
		: [this.currGroup.slides[0]];
	this.addNewGroup(slides);
	this.generateSets();
	this.draw(true);
}
/**
 * Drops the current group if allowed to be dropped
 */
SelectionGallery.prototype.closeSelection = function(){
	if (this.groups.length < 2) return;
	this.dropGroup();
	this.generateSets();
	this.draw(true);
}
/**
 * Loads an XML file referencing images into the selection gallery
 */
SelectionGallery.prototype.load = function(url){
	this.loader.load(url);
	this.setInfo("Loading Gallery...");
}
/**
 * Clears the gallery of all previously loaded images if they exist
 */
SelectionGallery.prototype.clearGallery = function(){
	var slides = this.groups[0].slides;
	var i = slides.length;
	while(i--){
		slides[i].remove();
	}
	this.groups = [];
	this.currGroup = null;
	this.underGroup = null;
	this.loadCount = 0;
	this.draw(true);
}
/**
 * Indicates that the XML content has been loaded
 */
SelectionGallery.prototype.contentLoaded = function(source){
	this.clearGallery();
	this.currGroup = new SGImageGroup(this, 0);
	this.groups.push(this.currGroup);
	var images = this.loader.images.slice();
	var n = images.length;
	var i;
	for (i=0; i<n; i++){
		this.currGroup.addNewSlide(images[i]);
	}
	this.draw(true);
}
/**
 * Indicates that a single slide has been loaded
 */
SelectionGallery.prototype.slideLoaded = function(source){
	this.loadCount++;
	var count = this.groups[0].slides.length;
	if (count == this.loadCount){
		this.updateInfo();
	}else{
		this.setInfo("Loading image "+this.loadCount+" of "+count+"...");
	}
	this.draw(true);
}
/**
 * Indicates that the user has selected one or more slides
 */
SelectionGallery.prototype.slidesSelected = function(){
	var slides = this.userSelection.slides;
	var n = slides.length;
	if (!n) return;
	var col;
	var i;
	switch(this.userSelection.selectionType){
		case SGUserSelection.SELECT:{
			if (this.groups.length <= 1
			||  slides.length != this.currGroup.slides.length){
				this.addNewGroup(slides);
				this.generateSets();
			}
			break;
		}
		case SGUserSelection.DESELECT:{
			if (this.groups.length > 1){
				if (slides.length == this.currGroup.slides.length){
					this.dropGroup();
					this.generateSets();
				}else if (this.underGroup){
					this.currGroup.dropSlides(slides, this.underGroup);
					this.generateSets();
					this.updateInfo();
					if (this.currGroup.slides.length == 1){
						this.currGroup.slides[0].loadFullImage();
					}
				}
			}
			break;
		}
		default:{
			return;
		}
	}
	this.draw(true);
}
/**
 * Calls the next set based on the slides next to
 * the slides in the current set in the set below
 */
SelectionGallery.prototype.nextSet = function(){
	var group = this.underGroup;
	if (!group) return;
	group.sets.push(group.sets.shift());
	this.dropGroup();
	this.addNewGroup(group.sets[0]);
	this.draw(true);
}
/**
 * Calls the previous set based on the slides next to
 * the slides in the current set in the set below
 */
SelectionGallery.prototype.prevSet = function(){
	var group = this.underGroup;
	if (!group) return;
	group.sets.unshift(group.sets.pop());
	this.dropGroup();
	this.addNewGroup(group.sets[0]);
	this.draw(true);
}
/**
 * Calculates the sets associated with the current selection
 * This is used for nextSet and prevSet
 */
SelectionGallery.prototype.generateSets = function(){
	var group = this.underGroup;
	if (!group) return;
	var setSlides = this.currGroup.slides.slice();
	group.sets = [];
	group.sets.push(setSlides);
	var indices = [];
	var slideHash = new Object();
	var i = setSlides.length;
	while (i--){
		slideHash[setSlides[i].index] = i;
	}
	var slideIndex;
	i = group.slides.length;
	while(i--){
		slideIndex = slideHash[group.slides[i].index];
		if (slideIndex != undefined){
			indices[slideIndex] = i;
		}
	}
	var n = group.slides.length;
	var currSet;
	do{
		currSet = this.getNewSet(group.slides, indices, slideHash);
		if (currSet){
			group.sets.push(currSet);
		}
	}while(currSet);
}
/**
 * Called by generateSets for the creation of a new set within the sets determined
 */
SelectionGallery.prototype.getNewSet = function(slides, indices, slideHash){
	var nextSet = [];
	var nextIndex;
	var n = indices.length;
	var i;
	for (i=0; i<n; i++){
		nextIndex = this.getNextIndex(slides, indices[i], slideHash);
		if (nextIndex != -1){
			indices[i] = nextIndex;
			slideHash[slides[nextIndex].index] = i;
			nextSet.push(slides[nextIndex]);
		}else{
			break;
		}
	}
	return nextSet.length ? nextSet : false;
}
/**
 * Finds the "next" index of a slide in the generation of sets.
 * If the actual next slide is already part of a set, the list of
 * slides is traversed until an available index is found
 */
SelectionGallery.prototype.getNextIndex = function(slides, index, slideHash){
	var nextIndex = -1;
	var n = slides.length;
	if (!n) return nextIndex;
	var i = index + 1;
	if (i >= n){
		i = 0;
	}
	while (i != index){
		if (slideHash[slides[i].index] == undefined){
			nextIndex = i;
			break;
		}
		i++;
		if (i >= n){
			i = 0;
		}
	}
	return nextIndex;
}

/**
 * Changes the scope of a function to another scope using the scope() mathod
 */
function SGEventHandler(){}
SGEventHandler.scope = function(method, scope){
	return function(){
		method.apply(scope, arguments.concat(this));
	}
}

/**
 * Loads XML content and creates SGImage instance to represent the information it contains
 */
function SGSourceLoader(gallery){
	this.images = [];
	this.gallery = gallery;
	this.imagesXml = new XML();
	this.imagesXml.ignoreWhite = true;
	this.imagesXml.onLoad = SGEventHandler.scope(this.contentLoad, this);
}
/**
 * Loads an xml file
 */
SGSourceLoader.prototype.load = function(url){
	this.imagesXml.load(url);
}
/**
 * Indicates when the XML has loaded
 */
SGSourceLoader.prototype.contentLoad = function(success){
	this.images = [];
	if (success){
		var atts;
		var imageNodes = this.imagesXml.firstChild.childNodes;
		var n = imageNodes.length;
		var i;
		for (i=0; i<n; i++){
			atts = imageNodes[i].attributes;
			this.images.push(new SGImage(atts.url, atts.thumbnailUrl, atts.title));
		}
		this.gallery.onContent(this);
	}
}
/**
 * Represents a group of images being viewed at any one time by the user
 */
function SGImageGroup(gallery, index, slides){
	this.gallery = gallery;
	this.index = index;
	this.sets = [];
	this.slides = [];
	if (slides){
		this.addSlides(slides);
	}
}
SGImageGroup.prototype.index = -1;
SGImageGroup.prototype.toString = function(){
	return "[object SGImageGroup ("+this.index+")]";
}
/**
 * Adds a selection of slides to the group
 */
SGImageGroup.prototype.addSlides = function(slides){
	slides = slides.slice();
	var n = slides.length;
	var i;
	for (i=0; i<n; i++){
		this.addSlide(slides[i]);
	}
}
/**
 * Adds a single slide to the group
 */
SGImageGroup.prototype.addSlide = function(slide){
	if (slide.group == this) return;
	slide.group = this;
	this.slides.push(slide);
}
/**
 * Creates a new slide for the group (this happens only once per image per XML loaded)
 */
SGImageGroup.prototype.addNewSlide = function(image){
	var depth = this.slides.length;
	var slideTarget = this.gallery.slideContainer.createEmptyMovieClip("slide"+depth, depth);
	var slide = new SGImageSlide(this.gallery, slideTarget, depth, image);
	this.addSlide(slide);
}
/**
 * Removes slides from this group associating them with the group passed
 */
SGImageGroup.prototype.dropSlides = function(slides, newGroup){
	newGroup = (newGroup) ? newGroup : null;
	var n;
	var i;
	if (!slides){
		n = this.slides.length;
		for (i=0; i<n; i++){
			this.slides[i].group = newGroup;
		}
		this.slides = [];
	}else{
		slides = slides.slice();
		n = slides.length;
		for (i=0; i<n; i++){
			this.removeSlide(slides[i], newGroup);
		}
	}
}
/**
 * Removes a slide from this group associating it with the group paseed
 */
SGImageGroup.prototype.removeSlide = function(slide, newGroup){
	newGroup = (newGroup) ? newGroup : null;
	var n = this.slides.length;
	var i;
	for (i=0; i<n; i++){
		if (this.slides[i] == slide){
			slide.group = newGroup;
			this.slides.splice(i, 1);
			break;
		}
	}
}
/**
 * Draws the group in the gallery window. Slides will be scaled down until all
 * slides can fit within the window in an square grid, remainders seen in the bottom row
 */
SGImageGroup.prototype.draw = function(minor){
	var firstGroup = this.gallery.groups[0];
	var isCurrGroup = Boolean(this == this.gallery.currGroup);
	var fogAmount = 1 - Math.pow(.5, this.gallery.currGroup.index - this.index);
	var baseDepth = 2*this.index*firstGroup.slides.length;
	var count = this.slides.length;
	var rows = Math.ceil(Math.sqrt(count));
	var cols = Math.ceil(count/rows);
	var scaleFactor = (cols > rows) ? 1/cols : 1/rows;
	var sWidth = scaleFactor*(this.gallery.availWidth + this.gallery.slideMargin);
	var sHeight = scaleFactor*(this.gallery.availHeight + this.gallery.slideMargin);
	var scale = (cols > rows)
		? 100*(this.gallery.availWidth - (cols - 1)*this.gallery.slideMargin)/(cols*this.gallery.availWidth)
		: 100*(this.gallery.availHeight - (rows - 1)*this.gallery.slideMargin)/(rows*this.gallery.availHeight);
	var slide;
	var lastRow = rows - 1;
	var colCount;
	var colOffset;
	var rowOffset;
	var i = rows*cols;
	var currCol;
	var currRow = rows;
	while (currRow--){
		colCount = (currRow == lastRow) ? (count - cols*lastRow) : cols;
		colOffset = this.gallery.centerX - sWidth*(colCount-1)/2;
		rowOffset = this.gallery.centerY + currRow*sHeight - sHeight*(rows-1)/2;
		currCol = cols;
		while (currCol--){
			i--;
			slide = this.slides[i];
			if (i < count && slide.loaded && slide.group == this){
				if (!minor){
					slide.draw();
				}
				slide.setTint(isCurrGroup ? null : this.gallery.backgroundColor, fogAmount);
				slide.setDestination(colOffset + currCol*sWidth, rowOffset, scale);
				slide.target.swapDepths(slide.tween ? baseDepth + count + i : baseDepth + i);
			}
			if (!i) break;
		}
		if (!i) break;
	}
}
/**
 * Removes all slides from the group
 */
SGImageGroup.prototype.clearContent = function(){
	var i = this.slides.length;
	while(i--){
		this.slides[i].remove();
	}
	this.slides = [];
}

/**
 * Contains an image as a slide object containing both the thumbnail
 * and the full size image when only the current slide is being viewed
 */
function SGImageSlide(gallery, target, index, image){
	this.gallery = gallery;
	this.target = target;
	this.index = index;
	this.image = image;
	this.thumbnailContainer = this.target.createEmptyMovieClip("thumbnailContainer", 0);
	this.thumbnail = this.thumbnailContainer.createEmptyMovieClip("thumbnail", 0);
	this.fullImageContainer = this.target.createEmptyMovieClip("fullImageContainer", 1);
	this.preloader = this.target.createEmptyMovieClip("preloader", 2);
	this.clearFullImage();
	this.target._x = this.gallery.centerX;
	this.target._y = this.gallery.centerY;
	this.target._xscale = 50;
	this.target._yscale = this.target._xscale;
	this.target.useHandCursor = false;
	this.target.trackAsMenu = true;
	this.target.onPress = SGEventHandler.scope(this.slideContact, this);
	this.target.onDragOver = SGEventHandler.scope(this.slideContact, this);
	this.target.onRollOver = SGEventHandler.scope(this.showToolTip, this);
	this.target.onRollOut = SGEventHandler.scope(this.gallery.toolTip.hide, this.gallery.toolTip);
	this.thumbnail.loadMovie(this.image.thumbnailUrl);
	this.thumbnailContainer.onEnterFrame = SGEventHandler.scope(this.thumbnailTestLoad, this);
}
SGImageSlide.prototype.loaded = false;
SGImageSlide.prototype.border = 3;
SGImageSlide.prototype.group = null;
SGImageSlide.prototype.tween = null;
SGImageSlide.prototype.destination = null;
SGImageSlide.prototype.destinationSteps = 6;
SGImageSlide.prototype.index = -1;
SGImageSlide.prototype.toString = function(){
	return "[object SGImageSlide ("+this.index+")]";
}
/**
 * Draws the slide fading its color based on its group location
 */
SGImageSlide.prototype.draw = function(){
	var w = this.gallery.availWidth;
	var h = this.gallery.availHeight;
	var w2 = w/2;
	var h2 = h/2;
	var b = this.gallery.slidePadding;
	this.target.clear();
	var hilite = SGGraphics.addColor(this.gallery.itemBackgroundColor, 0xFFFFFF, .75);
	var lolite = SGGraphics.addColor(this.gallery.itemBackgroundColor, 0x000000, .75);
	SGGraphics.simpleLinearGradient(this.target, -h2, h, hilite, lolite);
	this.drawSlideShape(w2, h2, b);
	this.target.endFill();
	hilite = SGGraphics.addColor(this.gallery.itemBackgroundColor, 0xFFFFFF, .20);
	lolite = SGGraphics.addColor(this.gallery.itemBackgroundColor, 0x000000, .20);
	SGGraphics.simpleLinearGradient(this.target, -h2, h, lolite, hilite);
	this.drawSlideShape(w2-this.border, h2-this.border, b-this.border/2);
	this.target.endFill();
	this.fitImage(this.thumbnail);
	this.fitImage(this.fullImage);
}
/**
 * Colorizes a slide by a specified amount
 */
SGImageSlide.prototype.setTint = function(hex, amount){
	var col = new Color(this.target);
	if (hex == undefined){
		col.setTransform({ra:100,rb:0,ga:100,gb:0,ba:100,bb:0,aa:100,ab:0});
	}else{
		var r = hex >> 16;
		var g = (hex >> 8) & 0xff;
		var b = hex & 0xff;
		var a = 100-100*amount;
		col.setTransform({ra:a,rb:r*amount,ga:a,gb:g*amount,ba:a,bb:b*amount,aa:100,ab:0});
	}
}
/**
 * Removes the full image being viewed in the slide revealing just the thumbnail
 */
SGImageSlide.prototype.clearFullImage = function(){
	this.preloader.clear();
	delete this.fullImageContainer.onEnterFrame;
	this.fullImage.unloadMovie();
	this.fullImage.removeMovieClip();
	this.fullImage = this.fullImageContainer.createEmptyMovieClip("fullImage", 0);
}
/**
 * Loads the full size version of the image into the slide for a single slide view
 */
SGImageSlide.prototype.loadFullImage = function(){
	if (this.fullImage._width) return;
	this.clearFullImage();
	this.fullImage.loadMovie(this.image.url);
	this.fullImageContainer.onEnterFrame = SGEventHandler.scope(this.fullImageTestLoad, this);
}
/**
 * Draws rounded rectangle shape for the slide
 */
SGImageSlide.prototype.drawSlideShape = function(w, h, b){
	this.target.moveTo(-w+b, -h);
	this.target.lineTo(w-b, -h);
	this.target.curveTo(w, -h, w, -h+b);
	this.target.lineTo(w, h-b);
	this.target.curveTo(w, h, w-b, h);
	this.target.lineTo(-w+b, h);
	this.target.curveTo(-w, h, -w, h-b);
	this.target.lineTo(-w, -h+b);
	this.target.curveTo(-w, -h, -w+b, -h);
}
/**
 * Fits an image to the shape of the slide
 */
SGImageSlide.prototype.fitImage = function(target){
	if (!target._width) return;
	target._xscale = 100;
	target._yscale = 100;
	var margin = 2*this.gallery.slideMargin;
	var slidePadding = 2*this.gallery.slidePadding;
	var w = this.gallery.availWidth - margin - slidePadding;
	var h = this.gallery.availHeight - margin - slidePadding;
	var scaleFactor = Math.min(w/target._width, h/target._height);
	target._xscale = 100 * scaleFactor;
	target._yscale = target._xscale;
	target._x = -target._width/2;
	target._y = -target._height/2;
}
/**
 * Removes a slide movie clip
 */
SGImageSlide.prototype.remove = function(){
	this.target.removeMovieClip();
}
/**
 * Polling function to check to see if the thumbnail has been
 * loaded by checking the size of the container movie clip
 */
SGImageSlide.prototype.thumbnailTestLoad = function(){
	if (this.thumbnail._width){
		this.loaded = true;
		this.draw();
		delete this.thumbnailContainer.onEnterFrame;
		this.gallery.onSlideLoaded(this);
	}
}
/**
 * Polling function to check to see if the full image has been
 * loaded by checking the size of the container movie clip
 * While testing, it also manages a preloader seen at the bottom of the slide
 */
SGImageSlide.prototype.fullImageTestLoad = function(){
	this.preloader.clear();
	if (this.fullImage._width){
		this.fitImage(this.fullImage);
		delete this.fullImageContainer.onEnterFrame;
	}else{
		var left = this.thumbnail._x;
		var bottom = this.thumbnail._y + this.thumbnail._height;
		var right = left + this.thumbnail._width;
		var top = bottom - this.gallery.faceBorder;
		var loaded = this.fullImage.getBytesLoaded();
		var total = this.fullImage.getBytesTotal();
		var percentLoaded = (total) ? loaded/total : 0;
		right =  left + (right-left)*percentLoaded;
		SGGraphics.simpleLinearGradient(this.preloader, top, bottom-top, this.gallery.backgroundColor, this.gallery.faceColor);
		this.preloader.moveTo(left, top);
		this.preloader.lineTo(right, top);
		this.preloader.lineTo(right, bottom);
		this.preloader.lineTo(left, bottom);
		this.preloader.lineTo(left, top);
		this.preloader.endFill();
	}
}
/**
 * Sets up a keyframe for a tween to move a scale a slide to
 */
SGImageSlide.prototype.setDestination = function(x, y, scale){
	var xr = Math.round(x);
	var yr = Math.round(y);
	var scaler = Math.round(scale);
	if (this.tween){
		var args = this.tween.args;
		if (Math.round(args.x2) == xr
		&&  Math.round(args.y2) == yr 
		&&  Math.round(args.scale2) == scaler){
			return;
		}
		this.tween.stop();
		delete this.tween;
	}
	if (Math.round(this.target._x) == xr
	&&  Math.round(this.target._y) == yr 
	&&  Math.round(this.target._xscale) == scaler
	&&  this.target._rotation == 0){
		return;
	}
	this.target._rotation = (this.target._x > x) ? 5 : -5;
	var args = {
		x:this.target._x, x2:x, spanX:x - this.target._x,
		y:this.target._y, y2:y, spanY:y - this.target._y,
		scale:this.target._xscale, scale2:scale, spanS:scale - this.target._xscale,
		r:this.target._rotation, r2:0, spanR:0 - this.target._rotation
	};
	this.tween = new SGTweener(this.target, "_xscale", this.target._xscale, scale, this.destinationSteps, this.ease, args);
	this.tween.onTween = SGEventHandler.scope(this.onTween, this);
	this.tween.onTweenComplete = SGEventHandler.scope(this.onTweenComplete, this);
	this.tween.startTween();
}
/**
 * Updates additional targets for a tween step; one tween is used per
 * slide and that tween only modifies one property
 */
SGImageSlide.prototype.onTween = function(){
	this.target._yscale = this.target._xscale;
	var args = this.tween.args;
	this.target._x = args.x + args.spanX*this.tween.easePercent;
	this.target._y = args.y + args.spanY*this.tween.easePercent;
	this.target._rotation = args.r + args.spanR*this.tween.easePercent;
}
/**
 * Removes a tween instance when a tween completes
 */
SGImageSlide.prototype.onTweenComplete = function(n){
	delete this.tween;
}
/**
 * Ease method for tweens
 */
SGImageSlide.prototype.ease = function(t){
	return 1 + Math.sin(1.88*t - 1.88)/.95;
}
/**
 * Detects when the mouse comes in contact with this slide and saves it to the
 * selection contacts array for managing selections
 */
SGImageSlide.prototype.slideContact = function(){
	this.gallery.toolTip.hide();
	var sel = this.gallery.userSelection;
	var n = sel.contacts.length;
	var i;
	for (i=0; i<n; i++){
		if (sel.contacts[i] == this){
			return;
		}
	}
	if (this.group == this.gallery.currGroup){
		sel.contacts.push(this);
	}
}
/**
 * Initiates a tooltip
 */
SGImageSlide.prototype.showToolTip = function(){
	if (this.group == this.gallery.currGroup){
		this.gallery.toolTip.show(this.image.title);
	}
}
/**
 * Removes a tooltip
 */
SGImageSlide.prototype.clearToolTip = function(){
	this.gallery.toolTip.hide();
}

/**
 * Contains image information extracted from XML
 */
function SGImage(url, thumbnailUrl, title){
	this.url = url;
	this.thumbnailUrl = thumbnailUrl;
	this.title = title;
}
SGImage.prototype.toString = function(){
	return "[image '"+this.title+"']"; 
}

/**
 * Base class for interactive objects (buttons) used in the gallery
 */
function SGButton(gallery, target, action, toolTipText){
	this.gallery = gallery;
	this.target = target;
	this.toolTipText = toolTipText;
	this.tab = this.target.createEmptyMovieClip("tab", 0);
	this.background = this.target.createEmptyMovieClip("background", 1);
	this.icon = this.target.createEmptyMovieClip("icon", 2);
	this.target.onRelease = SGEventHandler.scope(action, this);
	this.target.onRollOver = SGEventHandler.scope(this.buttonOver, this);
	this.target.onRollOut = SGEventHandler.scope(this.buttonOut, this);
	this.target.onDragOver = this.target.onRollOver;
	this.target.onDragOut = this.target.onRollOut;
	this.draw();
}
SGButton.prototype.size = 50;
SGButton.prototype.border = 5;
/**
 * Draws the button
 */
SGButton.prototype.draw = function(){
	this.size = this.gallery.hudHeight;
	this.border = this.size/10;
	this.tab.clear();
	this.tab.beginFill(this.gallery.faceColor, 100);
	this.drawTab(this.tab, this.size);
	this.tab.endFill();
	this.drawBackground(this.gallery.backgroundColor);
}
/**
 * Handles rollover for the button
 */
SGButton.prototype.buttonOver = function(){
	this.drawBackground(this.gallery.selectionColor);
	this.gallery.toolTip.show(this.toolTipText);
}
/**
 * handles rollout for the button
 */
SGButton.prototype.buttonOut = function(){
	this.drawBackground(this.gallery.backgroundColor);
	this.gallery.toolTip.hide();
}
/**
 * Draws background for the button; this differs based on rollover
 */
SGButton.prototype.drawBackground = function(hex){
	var size = this.size - this.border*2;
	var size2 = size/2;
	var hilite = SGGraphics.addColor(hex, 0xFFFFFF, .5);
	SGGraphics.simpleLinearGradient(this.background, -size2, size2, hilite, hex);
	this.drawCircle(this.background, size);
	this.background.endFill();
}
/**
 * Basic circle drawing command
 */
SGButton.prototype.drawCircle = function(target, size){
	if (target == undefined) target = this.target;
	var radius = size/2;
	var c1 = radius*(Math.SQRT2-1);
	var c2 = radius*(Math.SQRT2/2);
	target.moveTo(radius, 0);
	target.curveTo(radius, c1, c2, c2);
	target.curveTo(c1, radius, 0, radius);
	target.curveTo(-c1, radius, -c2, c2);
	target.curveTo(-radius, c1, -radius, 0);
	target.curveTo(-radius, -c1, -c2, -c2);
	target.curveTo(-c1, -radius, 0, -radius);
	target.curveTo(c1, -radius, c2, -c2);
	target.curveTo(radius, -c1, radius, 0);
}
/**
 * Draws a curved tab shape
 */
SGButton.prototype.drawTab = function(target, size){
	if (target == undefined) target = this.target;
	var radius = size/2;
	var c1 = radius*(Math.SQRT2-1);
	var c2 = radius*(Math.SQRT2/2);
	target.moveTo(radius, 0);
	target.curveTo(size - radius, c1, size - c2, c2);
	target.curveTo(size - c1, radius, size, radius);
	target.lineTo(-size, radius);
	target.curveTo(-size+c1, radius, -size+c2, c2);
	target.curveTo(-size+radius, c1, -size+radius, 0);
	target.curveTo(-radius, -c1, -c2, -c2);
	target.curveTo(-c1, -radius, 0, -radius);
	target.curveTo(c1, -radius, c2, -c2);
	target.curveTo(radius, -c1, radius, 0);
}
/**
 * Draws a cross
 */
SGButton.prototype.drawCross = function(target, size, thickness){
	if (target == undefined) target = this.target;
	var radius = size/2;
	var thick = thickness/2;
	target.moveTo(-thick, -radius);
	target.lineTo(thick, -radius);
	target.lineTo(thick, -thick);
	target.lineTo(radius, -thick);
	target.lineTo(radius, thick);
	target.lineTo(thick, thick);
	target.lineTo(thick, radius);
	target.lineTo(-thick, radius);
	target.lineTo(-thick, thick);
	target.lineTo(-radius, thick);
	target.lineTo(-radius, -thick);
	target.lineTo(-thick, -thick);
	target.lineTo(-thick, -radius);
}

/**
 * Previous button for navigating to the previous group
 */
function SGPrevButton(gallery, target){
	super(gallery, target, this.action, "Previous Set");
}
SGPrevButton.prototype = new SGButton();
/**
 * Draws the prev button with arrow
 */
SGPrevButton.prototype.draw = function(){
	super.draw();
	var radius = this.size/2 - this.border*2;
	this.icon.clear();
	this.icon.beginFill(this.gallery.faceColor, 100);
	this.icon.moveTo(-radius, 0);
	this.icon.lineTo(radius - this.border, -radius);
	this.icon.lineTo(radius - this.border, radius);
	this.icon.lineTo(-radius, 0);
}
/**
 * Calls the action for the prev button; loading the previous set
 */
SGPrevButton.prototype.action = function(){
	this.gallery.prevSet();
}

/**
 * Next button for navigating to the next group
 */
function SGNextButton(gallery, target){
	super(gallery, target, this.action, "Next Set");
}
SGNextButton.prototype = new SGButton();
/**
 * Draws the prev button with arrow
 */
SGNextButton.prototype.draw = function(){
	super.draw();
	var radius = this.size/2 - this.border*2;
	this.icon.clear();
	this.icon.beginFill(this.gallery.faceColor, 100);
	this.icon.moveTo(radius, 0);
	this.icon.lineTo(-radius + this.border, radius);
	this.icon.lineTo(-radius + this.border, -radius);
	this.icon.lineTo(radius, 0);
}
/**
 * Calls the action for the next button; loading the next set
 */
SGNextButton.prototype.action = function(){
	this.gallery.nextSet();
}

/**
 * Open button for opening the last group set or
 * the first single image in the current group
 */
function SGOpenButton(gallery, target){
	super(gallery, target, this.action, "Open Selection");
}
SGOpenButton.prototype = new SGButton();
/**
 * Draws the open button with a cross
 */
SGOpenButton.prototype.draw = function(){
	super.draw();
	this.icon.clear();
	this.icon.beginFill(this.gallery.faceColor, 100);
	this.drawCross(this.icon, this.size - this.border*4, this.border);
	this.icon.endFill();
}
/**
 * Calls the action for the open button; opening the gallery selection
 */
SGOpenButton.prototype.action = function(){
	this.gallery.openSelection();
}

/**
 * Close button for closing the current group
 */
function SGCloseButton(gallery, target){
	super(gallery, target, this.action, "Close Selection");
}
SGCloseButton.prototype = new SGButton();
/**
 * Draws the close button with an inverted cross
 */
SGCloseButton.prototype.draw = function(){
	super.draw();
	this.drawIcon(this.gallery.backgroundColor);
}
/**
 * Calls the action for the close button; closing the gallery selection
 */
SGCloseButton.prototype.action = function(){
	this.gallery.closeSelection();
}
/**
 * Overriding rollover handler to handle redrawing of inverted cross
 */
SGCloseButton.prototype.buttonOver = function(){
	super.buttonOver();
	this.drawIcon(this.gallery.selectionColor);
}
/**
 * Overriding rollout handler to handle redrawing of inverted cross
 */
SGCloseButton.prototype.buttonOut = function(){
	super.buttonOut();
	this.drawIcon(this.gallery.backgroundColor);
}
/**
 * Draws the inverted cross shape
 */
SGCloseButton.prototype.drawIcon = function(hex){
	var size = this.size - this.border*4;
	this.icon.clear();
	this.icon.beginFill(this.gallery.faceColor, 100);
	this.drawCircle(this.icon, size);
	this.icon.endFill();
	var size = this.size - this.border*2;
	var size2 = size/2;
	var hilite = SGGraphics.addColor(hex, 0xFFFFFF, .5);
	SGGraphics.simpleLinearGradient(this.icon, -size2, size2, hilite, hex);
	this.drawCross(this.icon, size, this.border);
	this.icon.endFill();
}

/**
 * Manages user gestures and selections with the mouse
 */
function SGUserSelection(gallery, target){
	this.contacts = [];
	this.gallery = gallery;
	this.target = target;
	this.selectTest = this.target.createEmptyMovieClip("selectTest", 0);
	this.lineDraw = this.target.createEmptyMovieClip("lineDraw", 1);
	this.target.onMouseDown = SGEventHandler.scope(this.selectPress, this);
	this.target.onMouseUp = SGEventHandler.scope(this.selectRelease, this);
}
SGUserSelection.SELECT = "select";
SGUserSelection.DESELECT = "deselect";
SGUserSelection.prototype.thickness = 0;
SGUserSelection.prototype.minThickness = 3;
SGUserSelection.prototype.maxThickness = 10;
SGUserSelection.prototype.thicknessFactor = 6;
SGUserSelection.prototype.last_xmouse = 0;
SGUserSelection.prototype.last_ymouse = 0;
SGUserSelection.prototype.selectionType = null;
/**
 * Initiates properties for starting a selection
 */
SGUserSelection.prototype.selectInit = function(){
	if (!this.target.onMouseMove){
		var mouseLoc = this.getDrawingMouse();
		this.slides = [];
		this.contacts = [];
		this.selectTest.clear();
		this.lineDraw.clear();
	}
}
/**
 * Begins the drawing/mouse gesture when the mouse is clicked
 */
SGUserSelection.prototype.selectPress = function(){
	var mouseLoc = this.getDrawingMouse();
	if (mouseLoc.clamped) return;
	if (!this.gallery.multiSelection){
		this.selectInit();
	}
	this.selectTest.beginFill(0x000000, 0);
	this.selectTest.moveTo(mouseLoc.x, mouseLoc.y);
	this.thickness = this.minThickness;
	this.lineDraw.lineStyle(this.thickness, this.gallery.selectionColor, 100);
	this.lineDraw.moveTo(mouseLoc.x, mouseLoc.y);
	this.directions = 0;
	this.last_xmouse = mouseLoc.x;
	this.last_ymouse = mouseLoc.y;
	this.target.onMouseMove = SGEventHandler.scope(this.selectMove, this);
}
/**
 * Handles mouse movement during a gesture checking for movement in all
 * directions to determine if the gesture is a selection or deselection
 */
SGUserSelection.prototype.selectMove = function(){
	var mouseLoc = this.getDrawingMouse();
	if (this.last_xmouse < mouseLoc.x){
		this.directions |= 1;
	}else if (this.last_xmouse > mouseLoc.x){
		this.directions |= 2;
	}
	if (this.last_ymouse < mouseLoc.y){
		this.directions |= 4;
	}else if (this.last_ymouse > mouseLoc.y){
		this.directions |= 8;
	}
	var dx = mouseLoc.x - this.last_xmouse;
	var dy = mouseLoc.y - this.last_ymouse;
	var dist = Math.sqrt(dx*dx, dy*dy);
	var thickness = Math.floor(dist/this.thicknessFactor);
	if (this.thickness > this.minThickness
	&&  thickness < this.thickness){
		this.thickness--;
	}else if (this.thickness < this.maxThickness
	&&  thickness > this.thickness){
		this.thickness++;
	}
	this.lineDraw.lineStyle(this.thickness, this.gallery.selectionColor);
	this.selectTest.lineTo(mouseLoc.x, mouseLoc.y);
	this.lineDraw.lineTo(mouseLoc.x, mouseLoc.y);
	this.last_xmouse = mouseLoc.x;
	this.last_ymouse = mouseLoc.y;
}
/**
 * Completes a gesture when the mouse is released
 */
SGUserSelection.prototype.selectRelease = function(){
	if (!this.target.onMouseMove) return;
	delete this.target.onMouseMove;
	this.selectTest.endFill();
	if (this.gallery.multiSelection) return;
	this.setSelection();
}
/**
 * Returns the location of the mouse within the bounds of the gallery slide area
 */
SGUserSelection.prototype.getDrawingMouse = function(){
	var x = this.target._xmouse;
	var y = this.target._ymouse;
	var clamped = false;
	var left = this.gallery.faceBorder;
	var right = this.gallery.width - this.gallery.faceBorder;
	var top = this.gallery.faceBorder;
	var bottom = this.gallery.height - this.gallery.faceBorder - this.gallery.hudHeight;
	if (x < left){
		x = left;
		clamped = true;
	}else if (x > right){
		x = right;
		clamped = true;
	}
	if (y < top){
		y = top;
		clamped = true;
	}else if (y > bottom){
		y = bottom;
		clamped = true;
	}
	return {x:x, y:y, clamped:clamped};
}
/**
 * When a selection is complete, select or deselect slides and clear drawing
 */
SGUserSelection.prototype.setSelection = function(){
	if (this.directions == 15){
		this.selectionType = SGUserSelection.SELECT;
		this.slides = this.getSelectedSlides();
	}else{
		this.selectionType = SGUserSelection.DESELECT;
		this.slides = this.contacts;
	}
	this.selectTest.clear();
	this.lineDraw.clear();
	this.gallery.onSelection(this);
	this.selectionType = null;
}
/**
 * Finds and returns all slides selected in the current gesture
 */
SGUserSelection.prototype.getSelectedSlides = function(){
	var selectedSlides = [];
	var slides = this.gallery.currGroup.slides;
	var graphic;
	var pt = new Object();
	var n = slides.length;
	var i;
	for (i=0; i<n; i++){
		graphic = slides[i].target;
		pt.x = graphic._x
		pt.y = graphic._y;
		graphic._parent.localToGlobal(pt);
		if (this.selectTest.hitTest(pt.x, pt.y, true)){
			selectedSlides.push(slides[i]);
		}
	}
	return selectedSlides;
}

/**
 * Gallery tooltips for buttons and slides
 */
function SGToolTip(gallery, target){
	this.gallery = gallery;
	this.target = target;
	this.target.createTextField("messageText", 0, 0, 0, 1, 1);
	this.messageText = this.target.messageText;
	this.messageText.autoSize = "left";
	this.messageText.selectable = false;
	var tf = this.messageText.getTextFormat();
	tf.font = "_sans";
	this.messageText.setNewTextFormat(tf);
	this.target._visible = false;
}
SGToolTip.prototype.padding = 1;
SGToolTip.prototype.offsetX = 10;
SGToolTip.prototype.offsetY = 20;
SGToolTip.prototype.text = "";
SGToolTip.prototype.delay = 1111;
SGToolTip.prototype.interval = -1;
SGToolTip.prototype.quickShow = false;
/**
 * Shows a tooltip after the specified delay
 */
SGToolTip.prototype.show = function(text, delay){
	this.text = text;
	if (delay != undefined) this.delay = delay;
	if (this.quickShow){
		this.reveal();
	}else{
		clearInterval(this.interval);
		this.interval = setInterval(this, "reveal", this.delay);
	}
}
/**
 * Draws a tooltip on the screen keeping it within the bounds of the movie
 */
SGToolTip.prototype.reveal = function(){
	if (this.text != undefined){
		this.target.clear();
		this.messageText.text = this.text;
		var bounds = this.target.getBounds(this.target);
		this.target.lineStyle(1, 0x333333);
		this.target.beginFill(0xFFFFCC);
		var left = bounds.xMin - 2*this.padding;
		var top = bounds.yMin - this.padding;
		var right = bounds.xMax + this.padding;
		var bottom = bounds.yMax + this.padding;
		this.target.moveTo(left, top);
		this.target.lineTo(right, top);
		this.target.lineTo(right, bottom);
		this.target.lineTo(left, bottom);
		this.target.lineTo(left, top);
		this.target.endFill();
	}
	this.quickShow = true;
	this.target._visible = true;
	clearInterval(this.interval);
	this.interval = setInterval(this, "revealTimeout", this.delay*2);
	this.target.onEnterFrame = SGEventHandler.scope(this.followMouse, this);
	this.followMouse();
}
/**
 * Hides the tooltip from view
 */
SGToolTip.prototype.hide = function(){
	this.target._visible = false;
	clearInterval(this.interval);
	this.interval = setInterval(this, "quickShowTimeout", this.delay/2);
	delete this.target.onEnterFrame;
}
/**
 * Timeout handler when the tooltip times out of quick show mode
 * and a full delay is again needed to view a tooltip
 */
SGToolTip.prototype.quickShowTimeout = function(){
	this.quickShow = false;
	clearInterval(this.interval);
	this.interval = -1;
}
/**
 * Timeout handler when the tooltip has been seen too long and needs to be hidden
 */
SGToolTip.prototype.revealTimeout = function(){
	this.quickShow = false;
	this.target._visible = false;
	clearInterval(this.interval);
	this.interval = -1;
	delete this.target.onEnterFrame;
}
/**
 * Handles the tooltip following the mouse every frame when visible
 */
SGToolTip.prototype.followMouse = function(){
	this.target._x = this.offsetX + this.padding + this.target._parent._xmouse;
	this.target._y = this.offsetY + this.padding + this.target._parent._ymouse;
	var bounds = this.target.getBounds(this.target);
	var pt = {x:bounds.xMax, y:bounds.yMax};
	this.target.localToGlobal(pt);
	var offsetX = pt.x - Stage.width;
	var offsetY = pt.y - Stage.height;
	if (offsetX > 0){
		this.target._x -= offsetX;
	}
	if (offsetY > 0){
		this.target._y -= offsetY;
	}
}

/**
 * Static graphics class for common graphics commands
 */
function SGGraphics(){}
/**
 * Sets up a simple, two-color, vertical linear gradient
 */
SGGraphics.simpleLinearGradient = function(target, y, height, hex1, hex2){
	var gradientMatrix = {matrixType:"box", x:0, y:y, w:100, h:height, r:Math.PI/2};
	target.beginGradientFill("linear", [hex1, hex2], [100, 100], [0, 0xFF], gradientMatrix);
}
/**
 * Adds a color to another color
 */
SGGraphics.addColor = function(base, blend, amount){
	var r1 = base >> 16;
	var g1 = (base >> 8) & 0xff;
	var b1 = base & 0xff;
	var r2 = blend >> 16;
	var g2 = (blend >> 8) & 0xff;
	var b2 = blend & 0xff;
	return (r1+(r2-r1)*amount) << 16 | (g1+(g2-g1)*amount) << 8 | (b1+(b2-b1)*amount);
}

/**
 * Tweens properties of an object via the onEnterFrame event
 */
function SGTweener(target, property, start, end, steps, ease, args){
	this.target = target;
	this.property = property;
	if (start != undefined) this.start = start;
	if (end != undefined) this.end = end;
	if (steps != undefined) this.steps = steps;
	if (ease != undefined) this.ease = ease;
	if (args != undefined) this.args = args;
	this.span = this.end - this.start;
}
SGTweener.broadcaster = null;
SGTweener.prototype.target = null;
SGTweener.prototype.property = null;
SGTweener.prototype.steps = 100;
SGTweener.prototype.percent = 0;
SGTweener.prototype.easePercent = 0;
SGTweener.prototype.start = 0;
SGTweener.prototype.end = 1;
SGTweener.prototype.value = 0;
SGTweener.prototype.args = null;
SGTweener.prototype.ease = function(n){
	return n;
}
/**
 * Tweener enter frame for working a tween over time
 */
SGTweener.prototype.onEnterFrame = function(){
	this.position++;
	this.draw();
	this.onTween(this);
	if (this.position >= this.steps){
		this.endTween();
	}
}
/**
 * Updates properties for the tween in action
 */
SGTweener.prototype.draw = function(){
	this.percent = this.position/this.steps;
	this.easePercent = this.ease(this.percent);
	this.value = this.start + this.span*this.easePercent;
	if (this.target) this.target[this.property] = this.value;
}
/**
 * Plays tween
 */
SGTweener.prototype.play = function(){
	this.draw();
	SGTweener.broadcaster.addListener(this);
}
/**
 * Stops tween
 */
SGTweener.prototype.stop = function(){
	SGTweener.broadcaster.removeListener(this);
}
/**
 * Starts tween from start
 */
SGTweener.prototype.startTween = function(){
	this.position = 0;
	this.percent = 0;
	this.play();
}
/**
 * Ends tween and resets
 */
SGTweener.prototype.endTween = function(){
	this.position = 0;
	this.percent = 0;
	this.stop();
	this.onTweenComplete(this);
}


//// APPLICATION ----------------------------------- ////

// restrict stage scaling
Stage.scaleMode = "noScale";
Stage.align = "TL";

// create a movie clip for the gallery to reside
var gallery = this.createEmptyMovieClip("gallery", 0);

// create a new instance of the SelectionGallery in the gallery
// movie clip loading the images.xml file for the gallery images
var sg = new SelectionGallery(gallery, 0, "images.xml");

// listen for key events for additional user interaction
// through the keyboard
Key.addListener(this);

// when the key is pressed, check for SHIFT to allow
// multiple selections
function onKeyDown(){
	switch (Key.getCode()){
		case Key.SHIFT:{
			sg.beginMultiSelection();
			break;
		}
	}
}

// When a key is released, look for arrow key interactions
// to navigate between sets (including opening and closing them)
function onKeyUp(){
	switch (Key.getCode()){
		case Key.LEFT:{
			sg.prevSet();
			break;
		}
		case Key.RIGHT:{
			sg.nextSet();
			break;
		}
		case Key.UP:{
			sg.openSelection();
			break;
		}
		case Key.DOWN:{
			sg.closeSelection();
			break;
		}
		
		// releasing SHIFT ends multiple selection
		case Key.SHIFT:{
			sg.endMultiSelection();
			break;
		}
	}
}