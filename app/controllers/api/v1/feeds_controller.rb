module Api
  module V1
    class FeedsController < ApplicationController
      def index
        feeds = Feed.order('created_at DESC');
        render json: {status: 'SUCCESS', message:'Loaded Feeds', data:feeds},status: :ok
      end

      def show
        article = Feed.find(params[:id])
        render json: {status: 'SUCCESS', message:'Loaded Feed', data:article},status: :ok
      end
    end
  end
end
