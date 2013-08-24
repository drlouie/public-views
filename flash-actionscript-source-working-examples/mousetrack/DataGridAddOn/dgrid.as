CellStyle = function()
{
}

CellStyle.prototype.getCellHeight = function()
{
   if( this.textStyle != undefined && this.textStyle.size != undefined )
      return this.textStyle.size + 12;

   return undefined;
}

FDataGridClass.prototype.drawHeaderBG = function()
{
	var tmp = this.header_mc.createEmptyMovieClip("headerBG", 1);

    var x_from = 0.75;

	for( var i = 0; i < this.colArray.length; i++ )
	{
	    var w = this.colArray[i].getWidth();

		tmp.moveTo( x_from, 1 );

		var bgCol = (this.styleTable.header.value==undefined) ? 0xaaaaaa : this.styleTable.header.value;

    	if( this.colArray[i].styleTable.headerBG.value != undefined )
		   bgCol = this.colArray[i].styleTable.headerBG.value;

		tmp.beginFill(bgCol);
		var bCol = (this.styleTable.gridLines.value==undefined) ? 0xdddddd : this.styleTable.gridLines.value;
		tmp.lineStyle(0,bCol);
		tmp.lineTo( x_from + w, 1 );
		tmp.lineStyle(0,bCol,100);
		tmp.lineTo( x_from + w, this.headerHeight );
		tmp.lineTo( x_from, this.headerHeight );
		tmp.lineStyle(0,0x000000,0);
		tmp.lineTo( x_from, 1 );

		tmp.endFill();

		x_from += w;
	}
}

// to be used any time the columns change width
FDataGridClass.prototype.drawColumns = function()
{
    this.drawHeaderBG();

//	var bg = this.createEmptyMovieClip("bg_mc", 2);
//	var lines = this.createEmptyMovieClip("lines_mc", 4);
	var x = 0.75;
	var oldX = 1;
	var tmpHeight = this.height - 1;

//	var mainBG = (this.styleTable.backGround.value == undefined) ? 0xffffff : this.styleTable.backGround.value;

	for( var i = 0; i < this.colArray.length; i++ )
   {
		x+=this.colArray[i].width;

		if (this.columnHeaders)
      {
			var lbl = this.header_mc["label"+i];
			lbl._x = oldX + 2;

			if (i==this.colArray.length-1)
				this.resizeColumn(i,this.colArray[i].width);

			lbl.setSize(this.colArray[i].width-5);
			this.header_mc["sep"+i]._x = x-1;
		}

		oldX = x;
	}

	for (var i=0; i<this.numDisplayed; i++)
   	this.rows[i].sizeColumns();

}

FGridRowClass.prototype.chooseRowCol = function(sel)
{
   var tmp = this.createEmptyMovieClip("highlight2", 1);

   var x_from = 1;

   for( var i = 0; i < this.controller.colArray.length; i++ )
   {
      var w = this.controller.colArray[i].getWidth();

      tmp.moveTo( x_from, 0 );

      var bgCol = ( this.controller.styleTable.backGround.value == undefined) ? 0xffffff : this.controller.styleTable.backGround.value;

      var cellBG = this.controller.getCellBackground( i, this.getItemIndex() );

      if( cellBG != undefined )
         bgCol = cellBG;
      else
         if( !this.controller.aRC || this.controller.colArray[i].styleTable.isRowAlternationVisible.value == false )
         {
            if( this.controller.colArray[i].styleTable.background.value != undefined )
               bgCol = this.controller.colArray[i].styleTable.background.value;
         }
         else
            bgCol = ( this.getItemIndex()%2 == 0 ) ? this.controller.row1 : this.controller.row2;

      if(sel)
      {
         var col = new Color( tmp );
         var myTObj = { ra: '45', rb: '0', ga: '45', gb: '0', ba: '45', bb: '0', aa: '30', ab: '0'};
         col.setTransform( myTObj );
      }

		var lineCol = (this.controller.styleTable.gridLines.value == undefined) ? 0x333333 : this.controller.styleTable.gridLines.value;

      tmp.beginFill( bgCol );
      tmp.lineStyle( 0, bgCol, 100 );

      tmp.lineTo( x_from + w - 1, 0 );

      if( i < this.controller.colArray.length - 1 && this.controller.gridLines )
      {
         tmp.lineStyle( 0, lineCol, 100 );
         tmp.lineTo( x_from + w - 1, this.highlight_mc._height );
         tmp.lineStyle( 0, bgCol, 100 );
      }
      else
         tmp.lineTo( x_from + w - 1, this.highlight_mc._height );

      tmp.lineTo( x_from, this.highlight_mc._height );

      tmp.lineTo( x_from, 0 );

      tmp.endFill();

      x_from += w;
   }
}

FGridRowClass.prototype.sizeColumns = function()
{
	var totX = 0;
	for (var i=0; i<this.controller.colArray.length; i++)
	{
		this.cells[i]._x = totX; // Math.floor
		this.cells[i].setSize(this.controller.colArray[i].width-4);
		this.cells[i].labelField.selectable = false;
		totX+=this.controller.colArray[i].width;
	}

   this.chooseRowCol(selected);

   if( this.controller.aRC && itmObj==undefined )
		this.highlight_mc._alpha = 0;
}

FGridRowClass.prototype.layoutContent = function(width)
{
	this.editHighlightSetup();
	var totX = 0;
	var offset = Math.floor((this.controller.itmHgt - this.controller.oldItmHgt) / 2);
	var maxHeight = 0;
	if( this.controller.colArray.length != 0 ) 
	{
		for( var i = 0; i < this.controller.colArray.length; i++ ) 
		{
         var tmpStyle;

         if( this.itemNum != undefined )
			   tmpStyle = this.controller.getCellTextStyle( i, this.getItemIndex() )

			if( tmpStyle == undefined )
  			   tmpStyle = this.controller.colArray[i].textStyle;

			if( tmpStyle == undefined ) 
				tmpStyle = this.controller.textStyle;
			
			this.cells[i] = this.attachMovie(this.controller.colArray[i].cellSymbol, "fCell"+i, 2+i, { hostComponent:this.controller, customTextStyle:tmpStyle, textStyle:tmpStyle }); 
			this.cells[i]._x = totX; // Math.floor
			this.cells[i]._y = offset;
			maxHeight = Math.max( maxHeight, this.cells[i].getHeight() );
			this.cells[i].setSize(this.controller.colArray[i].width-2);
			this.cells[i].labelField.selectable = false;
			this.cells[i].colIndex = i;
			this.cells[i].getGrid = this.controller.getGrid;
			this.cells[i].getCellIndex = this.controller.getCellIndex;
			totX+=this.controller.colArray[i].width;
			this.editCellSetup();
		}
		
		maxHeight = Math.max(this.controller.itmHgt, maxHeight);
		for (var i=0; i<this.controller.colArray.length; i++)
		{
			this.cells[i]._y = (maxHeight - this.cells[i]._height) / 2;
		}
	}
	else
	{
		this.cells[0] = this.attachMovie("FLabelSymbol", "fCell0", 2, {hostComponent:this.controller});
	}

   this.maxHeight = maxHeight;
}

FDataGridClass.prototype.getCellTextStyle = function( col, row )
{
	for( var i in this.cellStyles )
		if( this.cellStyles[i].colIndex == col && this.cellStyles[i].rowIndex == row )
			return this.cellStyles[i].textStyle;

	return undefined;
}

FDataGridClass.prototype.isCellHeightRedefined = function()
{
	for( var i in this.cellStyles )
		if( this.cellStyles[i].getCellHeight() != undefined )
			return true;

	return false;
}

FDataGridClass.prototype.getCellBackground = function( col, row )
{
	for( var i in this.cellStyles )
		if( this.cellStyles[i].colIndex == col && this.cellStyles[i].rowIndex == row )
			return this.cellStyles[i].background;

	return undefined;
}

FDataGridClass.prototype.getCellEditableFlag = function( col, row )
{
	for( var i in this.cellStyles )
		if( this.cellStyles[i].colIndex == col && this.cellStyles[i].rowIndex == row )
			return this.cellStyles[i].editable;

	return undefined;
}

FDataGridClass.prototype.isCellEditable = function( col, row )
{
   if( this.editable != true ) return false;

	for( var i = 0; i < this.cellStyles.length; i++ )
		if( this.cellStyles[i].colIndex == col
          && this.cellStyles[i].rowIndex == row
          && this.cellStyles[i].editable != undefined )
			return this.cellStyles[i].editable;

   if( this.colArray[ col ].editable == false )
     return false;

	return true;
}

FDataGridClass.prototype.setCellStyle = function( col, row, propName, value )
{
	if( this.cellStyles == undefined )
	   this.cellStyles = new Array();

	var found;

	for( var i = 0; i < this.cellStyles.length; i++ )
		if( this.cellStyles[i].colIndex == col && this.cellStyles[i].rowIndex == row )
			found = i;

	if( found == undefined )
	{
		var cell_style = new CellStyle();
		cell_style.colIndex = col;
		cell_style.rowIndex = row;
		cell_style.rowID = this.dataProvider.getItemID( row )
		found = this.cellStyles.push( cell_style ) - 1;
	}

	if( propName.subString( 0, 4 ) == "text" )
	{
		if( this.cellStyles[ found ].textStyle == undefined )
			this.cellStyles[ found ].textStyle = new TextFormat();

		var textProp = propName.subString( 4, propName.length );
		this.cellStyles[ found ].textStyle[ textProp ] = value;
		this.invalidate("setSize");
		return true;
	}
   else
   {
		var cell_style = this.cellStyles[ found ];
      cell_style[ propName ] = value;
      return true;
   }

	return undefined;
}

FDataGridClass.prototype.modelChanged = function(eventObj)
{
	super.modelChanged(eventObj);

	if (eventObj.event == "sort")
	{
		for( var i in this.cellStyles )
		{
			for( var row = 0; row < this.getLength(); row++ )
		    	if( this.cellStyles[i].rowID == this.dataProvider.getItemID( row ) )
				{
					this.cellStyles[i].rowIndex = row;
					break;
				}
		}

      if( this.isCellHeightRedefined() == true )
      	this.invalidate("relayoutRows");

		return;
	}

	this.initScrollBar();
	this.invalidate("drawColumns");
	this.invalidate("initHeaders");
}


FSelectableListClass.prototype.setSize = function(w, h)
{
	super.setSize(w,h);
	this.boundingBox_mc._xscale = this.boundingBox_mc._yscale = 100;
	this.boundingBox_mc._xscale = this.width * 100 / this.boundingBox_mc._width;
	this.boundingBox_mc._yscale = this.height * 100 / this.boundingBox_mc._height;

   var y = 0;

	for (var i = 0; i < this.numDisplayed; i++)
   {
		this.rows[i] = this.container_mc.attachMovie(this.itemSymbol, "row" + i + "_mc", 10 + i, {controller:this,itemNum:i});
		this.container_mc[ "fListItem" + i + "_mc" ] = this.rows[i];
		var offset = ( this.scrollOffset == undefined ) ? 0 : this.scrollOffset;
		this.rows[i].setSize( this.width-offset, this.rows[i].maxHeight );
		this.rows[i]._y = y;

      y += this.rows[i].maxHeight;
	}

	this.updateControl();
}

FSelectableItemClass.prototype.setSize = function(width, height)
{
	this.width = width;
	this.layoutContent(width); // EXTEND this for alternate content.

	if (this.highlight_mc==undefined)
   {
		this.attachMovie( "FHighlightSymbol", "highlight_mc", LOWEST_DEPTH);
		this.highlight_mc._x=1;
		this.highlight_mc.controller = this;
		this.highlight_mc._alpha = 0;
		this.highlight_mc.trackAsMenu = true;
		this.highlight_mc.useHandCursor = false;
		this.highlight_mc.onPress = this.highlightPress;
		this.highlight_mc.onDragOver = this.highlightDragOver;

	}

	this.highlight_mc._width = width-0.5;
	this.highlight_mc._height = Math.max( height, this.maxHeight );
}

FDataGridClass.prototype.setSize = function(w,h)
{
	if (!this.enable)
		return;

	this._yscale = this._xscale = 100;
	delete this.methodTable["setSize"];

	if (this.borderOn)
		this.boundingBox_mc._visible = true;

	this.width = Math.max(w, 20);
	this.height = Math.max(h, 40);
	this.container_mc.removeMovieClip();
	this.scrollBar_mc = undefined;
	this.container_mc = this.createEmptyMovieClip("container", 3);

	var headerH = 0;

	if (this.columnHeaders)
   {
		this.initHeaders();
		headerH = this.header_mc._height;
		this.container_mc._y = headerH;
	}

   this.relayoutRows();

	this.initHeaders();
	this.colArray[this.colArray.length-1].setWidth(this.colArray[this.colArray.length-1].width);
	this.drawColumns();
	delete this.methodTable["drawColumns"];
}

FDataGridClass.prototype.relayoutRows = function()
{
	var headerH = this.header_mc._height;
   var w = this.width;
   var h = this.height;

	this.measureItmHgt();
	this.oldItmHgt = this.itmHgt;

	if( this.rowHeight != undefined && this.itmHgt < this.rowHeight )
   {
		this.itmHgt = this.rowHeight;
	}

	if( this.tmpRowCount != undefined )
   {
		this.numDisplayed = this.tmpRowCount;
		delete this.tmpRowCount;
    	this.height = this.numDisplayed * (this.itmHgt-2) + 2 + headerH;
	}
   else
      if( this.rowHeight != undefined )
      {
         this.numDisplayed = Math.floor( ( h - headerH ) / ( this.itmHgt - 2 ) );
      	this.height = this.numDisplayed * ( this.itmHgt - 2 ) + 2 + headerH;
      }
      else
      {
         var total_height = 0;
         var rows_to_display = 0;

         var r = this.getScrollPosition();

         while( total_height < h - headerH )
         {
            var row_height = 0;

            for( var i in this.cellStyles )
               if( this.cellStyles[i].rowIndex == r )
               {
                  var cell_h = this.cellStyles[i].getCellHeight();

                  if( cell_h != undefined && cell_h > row_height)
                     row_height = cell_h - 2;
               }

            if( row_height == 0 )
               row_height = this.itmHgt;

            if( headerH + total_height + row_height - h < row_height / 2 )
            {
               total_height += row_height;
               rows_to_display++;
            }
            else
               break;

            r++;
         }

         this.numDisplayed = rows_to_display;
         this.height = total_height + headerH;
      }

	super.setSize(w, this.height);

	this.scrollBar_mc._y-=headerH;
}

FGridRowClass.prototype.displayContent = function(itmObj, selected)
{
	if( itmObj.label == "Sizer: PjtTopg" )
   {
		this.fCell0.setValue(itmObj.label, selected);
		return;
	}

	if( this.highlighted != selected || this.redraw )
   {
		var prop = (selected) ? "textSelected" : "textColor";
		if(!this.enable)
			prop = "textDisabled";

		var clr = this.controller.styleTable[prop].value;

		if (clr==undefined)
      {
			clr = (selected) ? 0xffffff : 0x000000;
			if (!this.enable)
				clr = 0x666666;
		}
	}

	var i = this.cells.length;

	while (i--)
   {
      var native_value = itmObj[ this.controller.colArray[i].colName ];

    	if( this.cells[i].labelField.type == "input" )
      {
         this.cells[i].setValue( native_value, selected );
      }
      else
      {
         if( this.controller.colArray[i].displayConverter != undefined )
         {
		      native_value = _root[ this.controller.colArray[i].displayConverter ]( native_value );
            this.cells[i].setValue( native_value, selected );
         }
         else
            if( native_value != undefined )
            {
               if( this.controller.colArray[i].displayFactor )
                  native_value = Number( native_value ) * this.controller.colArray[i].displayFactor;

               var tmp_text = "";

               if( this.controller.colArray[i].displayPrefix != undefined )
                  tmp_text = tmp_text + this.controller.colArray[i].displayPrefix;

               tmp_text = tmp_text + String( native_value );

               if( this.controller.colArray[i].displayPostfix != undefined )
                  tmp_text = tmp_text + this.controller.colArray[i].displayPostfix;

               this.cells[i].setValue( tmp_text, selected );
            }
      }

      if( this.controller.isCellEditable( i, this.getItemIndex() ) == true )
      {
         this.cells[i].labelField.border = this.controller.editableBorder;
         this.cells[i].labelField.borderColor = this.controller.editableBorderColor;
         this.cells[i].labelField.background = this.controller.editableBackground;
         this.cells[i].labelField.backgroundColor = this.controller.editableBackgroundColor;
      }

		if( this.highlighted != selected || this.redraw )
      {
			var colClr = this.controller.colArray[i].styleTable[prop].value;

			if( colClr == undefined )
				colClr = clr;

			this.cells[i].setColor( colClr );
		}
	}

   this.chooseRowCol(selected);

   if( this.controller.aRC && itmObj==undefined )
		this.highlight_mc._alpha = 0;

	delete this.redraw;
}

// this is the highlight_mc - controller is the row
FGridRowClass.prototype.startEditCell = function()
{
	var grid = this.controller.controller;
	if(this.controller.enable)
   {
  	   if(grid.editable)
      {
			for( var i=0; i<this.controller.cells.length; i++ )
         {
            var is_editable = grid.getCellEditableFlag( i, this.controller.getItemIndex() );

				if(is_editable == true || ( is_editable == undefined && grid.colArray[i].editable == true ) )
            {
					if (this.controller.cells[i].hitTest(_root._xmouse, _root._ymouse))
               {
						grid.selectedCell = { index: this.controller.getItemIndex(), colName: grid.colArray[i].colName };

						grid.setSelectedCell(this.controller.getItemIndex(), grid.colArray[i].colName);

						clearInterval(grid.dragScrolling);
						delete grid.onMouseUp;
						return;
					}
				}
			}
		}
	}
}

FDataGridClass.prototype.setSelectedCell = function(index, colName)
{
	if (!this.enable || !this.editable) return;

//	Selection.setFocus(this);

	var rowIdx = index-this.topDisplayed;
	var colIdx = this.getColumnIndex(colName);

   var itemObj = this.rows[rowIdx].getItemModel();
   this.rows[rowIdx].cells[colIdx].setValue( itemObj[ this.colArray[colIdx].colName ], this.rows[rowIdx].highlighted );

	if (this.topDisplayed>index || index>=this.topDisplayed+this.numDisplayed)
		this.setScrollPosition(index);

	this.rows[rowIdx].lastEdited = this.rows[rowIdx].cells[colIdx].getLabel();
	this.rows[rowIdx].cells[colIdx].labelField.controller = this.rows[rowIdx];
	this.selectedCell = { index: index, colName: colName };
	Selection.removeListener(_global._focusControl);

	this.rows[rowIdx].cells[colIdx].setFocus();
}

// in this case, this is a textField, controller is the row.
FGridRowClass.prototype.cellBlurred = function()
{
//	trace("cellBlurred " + this.cellNum + " " + this.controller.itemNum + this);
	this.selectable = false;
	this.type = "dynamic";
	this.hscroll=0;
	this.background = false;
	this.border = false;
	var grid = this.controller.controller;

	grid.editCell(this.cellNum, this.controller.itemNum, this.controller.cells[this.cellNum].getLabel());

	var caught = grid.catchTab(this.controller.getItemIndex(), grid.colArray[this.cellNum].colName);
	if (!caught)
   {

		Key.removeListener(_global.FGridKeyListener);
		delete _global.FGridKeyListener;
		Selection.addListener(_global._focusControl);
	}

   var itemObj = this.controller.getItemModel();
   this.controller.displayContent( itemObj, this.controller.highlighted );
}

