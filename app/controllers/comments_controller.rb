class CommentsController < ApplicationController

  def index
    @comments = Comment.order('created_at DESC')
  end

end
